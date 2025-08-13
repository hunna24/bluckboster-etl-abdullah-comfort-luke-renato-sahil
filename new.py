import streamlit as st
import pandas as pd
from main import df_loaded


st.image("images/Logo.png", width=220)
df = pd.read_csv("output.csv")
# centered title
st.markdown("""<style> h1 {text-align: center;} </style>""", unsafe_allow_html=True)

movies = df['title'].drop_duplicates().sort_values()

st.title("BluckBoster")
st.write("Search for films, check availability and see where they can be rented")

movies = (
    df_loaded["title"]
    .dropna()
    .astype(str)
    .drop_duplicates()
    .sort_values()
    .tolist()
)

movie_info = st.selectbox("Select a movie", movies, index=0)

selected_movie = df_loaded[df_loaded['title'] == movie_info].iloc[0]


#display movie details
st.subheader(selected_movie['title'])
st.text(f"Rating: {selected_movie['rating']}")
st.text(f"Runtime: {selected_movie['length']} minutes")
st.text(f"Release Year: {selected_movie['release_year']}")
st.text(f"Description: {selected_movie['description']}")
st.text(f"Language: {selected_movie['language']}")
st.text(f"Category: {selected_movie['category_name']}")


Cities = (
    df_loaded["store_city"]
    .dropna()
    .astype(str)
    .drop_duplicates()
    .sort_values()
    .tolist()
)
selected_city = st.selectbox("Select your city", Cities, index=0)

city_movie_df = df_loaded[
    (df_loaded['store_city'] == selected_city) &
    (df_loaded['title'] == selected_title)
]

# city_movie_df['available'] = city_movie_df.apply(
#     lambda row: pd.isna(row['rental_date']) or pd.notna(row['return_date']),
#     axis=1
# )

# if city_movie_df.empty:
#     st.write("This movie is not available in your selected city")
# else:
#     st.text(f"Availability in {selected_city}:")
#     for _, row in city_movie_df.iterrows():
#         status = "Available" if row['available'] else "Not Available"
#         st.text(f" - {row['store_name']}: {status}")



