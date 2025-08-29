import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=51bd66bdf873b3703a97d6af75403b1b".format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original'+data['poster_path']


#function for movie recommand that is used in button below
def recommand(movie):
    if movie not in movies['title'].values:
        print(f"Movie '{movie}' not found in the dataset.")
        return

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommanded_movies=[]
    recommanded_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommanded_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommanded_movies_poster.append(fetch_poster(movie_id))
    return recommanded_movies,recommanded_movies_poster

#3rd  import movies and similarity df
#formaning a dataframe for movies title
#import statement for movies
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

#import statement for similarity
similarity=pickle.load(open('similarity.pkl','rb'))

# 1st set movie title
st.title('Movie Recommendation System')

# 2nd the selection button(selectbox)
#option button for movie selection
selected_movie_name=st.selectbox(
    'Select a movie to recommand',
movies['title'].values)

#button for recommendation
if st.button("Recommend"):
    names,posters = recommand(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])



