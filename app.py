
import streamlit as st
import pickle

# Load the DataFrame of movies
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie_title):
    # Find index of the selected movie
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommender System')

movies_list = movies['title'].values
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies_list
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
