# Movie-Recommender-System

**Deployed application can be found at:** https://recommender-project-engage.herokuapp.com/

Content Based Recommender System recommends movies similar to the movie user likes and the movies that have similar genres or storylines.

Data is taken from TMDB 5000 Movie Dataset, https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv, and posters have benn fetched using an 
API by TMDB, https://www.themoviedb.org/documentation/api

## Movie Recommender System
This is content based recommender system that recommends movies based on Movies and Genres that uses nearest neighbours algorithms using cosine similarity. I have created this project as a challenge in Microsoft Engage'2022.
I created the frontend using [Streamlit](https://streamlit.io/) and deployed the application on [Heroku](https://www.heroku.com/).

## Screenshots
![Screenshot (561)](https://user-images.githubusercontent.com/79306021/170832832-97e534b3-f4dc-4d9b-87c5-bf3c1f76a29b.png)
![Screenshot (562)](https://user-images.githubusercontent.com/79306021/170832920-0cf22d7d-7da7-416b-9d94-78e3a467be5e.png)
![Screenshot (563)](https://user-images.githubusercontent.com/79306021/170833906-319d50a0-c7a4-4c98-9687-cb20d647ed6a.png)

## Features
- Simple responsive UI
- Movie based and Genres based recommendations
- Movie Posters and Directors 
- Give your ratings⭐

## How to get the API key?

Create an account in https://www.themoviedb.org/, go to your account settings, click on the `API` link from the left hand sidebar. Fill all the details to apply 
for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## How to run the project?

1. Clone or download this repository to your local machine.
2. Install all the required libraries with the command `pip install -r requirements.txt`
3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
3. Replace YOUR_API_KEY in **both** the places (line no. 20) of `app/app.py` file and hit save.
4. Open your terminal/command prompt from your project directory, go inside the app folder and run the file `app.py` by executing the command `streamlit run app.py`.
5. It will automatically open the application in your default browser.
6. Hurray! That's it.

## Similarity Score : 

   How does it decide which item is most similar to the item user likes? Here come the similarity scores.
   
   It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. 
   This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of 
   similarity between given text details of two items. This can be done by cosine-similarity.
   
## How Cosine Similarity works?
  Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the 
  angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far 
  apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the 
  cosine similarity.
  
  ![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

  
More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)
