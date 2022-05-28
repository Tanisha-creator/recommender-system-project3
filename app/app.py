import pickle
import numpy as np
import streamlit as st
import requests
from PIL import Image
import random
import string

# Loading pickle files
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
genreList = pickle.load(open('genreList.pkl','rb'))

# List of all Genres of movies
movie_genres = ['Action','Adventure','Animation','Comedy','Crime','Documentary','Drama','Family','Fantasy','Foreign',
 'History','Horror','Music','Mystery','Romance','ScienceFiction','TVMovie','Thriller','War','Western']

# Function to fetch the movie_poster through API
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=07435124a9f1c82ffaa0b5ae689fc8c1&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to return Recommended-movies and movie-poster
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

# Function to Recommend movies on Genres Based
def genre_check(options):
    for idx, word in enumerate(genreList):
        # print(a)
        count=0
        if (np.isin(options, word)).any():
            count=count+1
            movie_id = movies.iloc[idx].movie_id
            recommended_movie_posters=fetch_poster(movie_id)
            recommended_movie_names=movies.iloc[idx].title
            #recommended_movie_taglines = movies.iloc[idx].tagline
            recommended_movie_crew = movies.iloc[idx].crew[0]

            st.image(recommended_movie_posters, width=300)
            st.text(recommended_movie_names)
            #st.text('Tagline: ' + recommended_movie_taglines)
            st.text('Directed by: ' + recommended_movie_crew)
        if(count==5):
            break

# Frontend part
st.markdown("<h1 style='text-align: center; color: yellow;'>Movie Recommender System</h1>", unsafe_allow_html=True)
img1 = Image.open('movie-time.jpg')
img1 = img1.resize((250,250),)
st.image(img1,width=300)
st.header('What to watch next? 🤔')

# Movie-based dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# column of Recommended movies
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)

    st.success('Some of the movies from our Recommendation, have a look below')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

# Ratings slider
x = st.slider('Your Ratings 🌟😊',2,5)

# NOTE: Streamlit framework doesn't allow looping or custom functions so code snippets has to be repeated

def autocolumn(i):
	temp1=[]
	for x in range(i):
		temp1.append(random.choice(string.ascii_uppercase)+str(x))
	if i == 2:
		temp1[0:1]=st.columns(2)
		with temp1[0]:
			st.markdown(":star:")
		with temp1[1]:
			st.markdown(":star:")

	elif i == 3:
		temp1[0:2]=st.columns(3)
		with temp1[0]:
			st.markdown(":star:")
		with temp1[1]:
			st.markdown(":star:")
		with temp1[2]:
			st.markdown(":star:")
	elif i == 4:
		temp1[0:3]=st.columns(4)
		with temp1[0]:
			st.markdown(":star:")
		with temp1[1]:
			st.markdown(":star:")
		with temp1[2]:
			st.markdown(":star:")
		with temp1[3]:
			st.markdown(":star:")
	elif i == 5:
		temp1[0:4]=st.columns(5)
		with temp1[0]:
			st.markdown(":star:")
		with temp1[1]:
			st.markdown(":star:")
		with temp1[2]:
			st.markdown(":star:")
		with temp1[3]:
			st.markdown(":star:")
		with temp1[4]:
			st.markdown(":star:")

autocolumn(x)

# Genres based dropdown
options = st.multiselect('Select Genres:', movie_genres)
if options:
    genre_check(options)
    st.text(options)

st.markdown("<h6 style='text-align: center; color: yellow;'>Made by Tanisha Kindo</h6>", unsafe_allow_html=True)