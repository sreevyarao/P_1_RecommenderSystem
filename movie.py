import streamlit as st
import pickle
import pandas as pd
import os
import streamlit as st
import time
import warnings
warnings.filterwarnings("ignore")
if "selected_trailer" not in st.session_state:
    st.session_state.selected_trailer = None

TRAILERS = {
    "Titan A.E.": "https://www.youtube.com/watch?v=njRH_EDfLpA","Pirates of the Caribbean: Dead Man's Chest": "https://youtu.be/SNA-Ezahmok?si=7_mS60dMGMcuFvSV",
    "Small Soldiers": "https://youtu.be/l3EMhIo1fVo?si=IZ2zfd4RutQ55ham","Pirates of the Caribbean: On Stranger Tides": "https://youtu.be/0BXCVe8Yww4?si=pwpmEYHurFMSKwIT",
    "Independence Day": "https://www.youtube.com/watch?v=B1E7h3SeMDk","Pirates of the Caribbean: The Curse of the Black Pearl": "https://youtu.be/naQr0uTrH_s?si=7mXo9n2sKZl8qj3k", 
    "Ender's Game": "https://www.youtube.com/watch?v=2SRizeR4MmU","20,000 Leagues Under the Sea": "https://youtu.be/BdHWQOhs1x4?si=JIiS8ufRnWSsN_RN",
    "Aliens vs Predator: Requiem": "https://youtu.be/XbTWLrZLYmU?si=xu233PiPZXuKR92c","Puss in Boots": "https://youtu.be/1esRrwrmWzA?si=WDCvtSqTZ5Pvykk4",
    "Spider-Man":"https://youtu.be/t06RUxPbp_c?si=WXT6Y3ji7zfIGWwN",
    "Spider-Man 2":"https://youtu.be/kficMW9vu8M?si=vyEXO7YBKTcr9MuQ",
    "The Amazing Spider-Man 2":"https://youtu.be/DlM2CWNTQ84?si=UBt5iJeKakXTRUfs",
    "The Amazing Spider-Man":"https://youtu.be/-tnxzJ0SSOw?si=VgZzEWpbDndg4PQ7",
    "Arachnophobia":"https://youtu.be/p2EZkRcw3LA?si=O-Xfwj8riFHxXhQx",
    "Out of Inferno": "https://youtu.be/GCPRkTzYMko?si=2plz9ezI1hnT8A9j",
    "Aladdin": "https://youtu.be/k6XwVbCPC5Y?si=oYlT9lv37N2EJrgU",
    "Toy Story 3": "https://youtu.be/DFTIL0ciHik?si=Cl5YM0csU47Keogk",
    "The Princess and the Frog": "https://www.youtube.com/watch?v=uQBy6jqbmlU",
    "Frozen": "https://www.youtube.com/watch?v=TbQm5doF_Uc","The Dark Knight":"https://www.youtube.com/watch?v=EXeTwQWrcwY",
    "Iron Man":"https://youtu.be/oDOf1BXPyfg?si=K_dx1jeUBpZK9J5-","Batman Begins":"https://youtu.be/neY2xVmOfUM?si=98EbJfMmiNaqW9j5",
    "Iron Man 2":"https://youtu.be/BoohRoVA9WQ?si=7n2sXo7l3j1mLh5b","Batman":"https://youtu.be/mqqft2x_Aa4?si=hYrbRQzFuhGvxEHX",
    "Iron Man 3":"https://youtu.be/Ke1Y3P9D0Bc?si=9n2sXo7l3j1mLh5b","Batman Returns":"https://youtu.be/repBHGIny0c?si=g1itLCDoztP6NkCL",
    "The Avengers":"https://youtu.be/eOrNdBpGMv8?si=9n2sXo7l3j1mLh5b","Captain America: Civil War":"https://youtu.be/dKrVegVI0Us?si=9n2sXo7l3j1mLh5b"
}


# ---------------- SPLASH SCREEN ----------------
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(
            rgba(0,0,0,0.85),
            rgba(0,0,0,0.95)
        ),
        url("https://images.unsplash.com/photo-1606112219348-204d7d8b94ee");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    @keyframes zoomFade {
        0% {
            opacity: 0;
            transform: scale(0.6);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    .filmflix-logo {
        font-size: 80px;
        font-weight: 900;
        color: #E50914;
        text-align: center;
        margin-top: 180px;
        letter-spacing: 6px;
        animation: zoomFade 2.5s ease-out forwards;
        text-shadow: 0px 0px 30px rgba(229,9,20,0.9);
    }

    .subtitle {
        text-align: center;
        color: white;
        font-size: 18px;
        margin-top: 20px;
        opacity: 0;
        animation: zoomFade 2s ease-out forwards;
        animation-delay: 1.5s;
    }

    </style>
    """, unsafe_allow_html=True)

    # 🎬 Animated Logo
    st.markdown("<div class='filmflix-logo'>FILMFLIX</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Your cinematic universe begins…</div>", unsafe_allow_html=True)


    # ⏳ splash delay
    time.sleep(4)

    #  move to main app
    st.session_state.loaded = True
    st.rerun()
    
# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ---------------- NETFLIX STYLE CSS ----------------
st.markdown("""
    <style>
    .stApp {
    background: linear-gradient(
        rgba(0, 0, 0, 0.75),
        rgba(0, 0, 0, 0.85)
    ),
    url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

body {
    background-color: #0f0f0f;
}

.main {
    background: linear-gradient(to bottom, #141414, #000000);
    color: white;
}

h1 {
    color: #E50914;
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    letter-spacing: 2px;
}
   /* Make only headings white */
h1, h2, h3, h4, h5 {
    color: #ffffff !important;
}

/* Make normal paragraph text white */
p {
    color: #ffffff !important;
}
        
}
h2 {
    font-weight: bold;
    text-shadow: 0px 0px 12px rgba(255,255,255,0.5);
}


.stSelectbox label {
    font-size: 20px;
    color: red;
}

.stButton>button {
    background-color: #E50914;
    color: white;
    border-radius: 8px;
    height: 50px;
    width: 220px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #ff1f1f;
    transform: scale(1.05);
}

img {
    border-radius: 15px;
    transition: transform 0.3s;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
}

img:hover {
    transform: scale(1.08);
}

footer {
    visibility: hidden;
}
/* Fix selected value inside white selectbox */
div[data-baseweb="select"] span {
    color: black !important;
}


</style>
""", unsafe_allow_html=True)


# ---------------- LOAD DATA ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Load movie dictionary
movies_dict = pickle.load(open(os.path.join(BASE_DIR, 'movie_dict.pkl'), 'rb'))

# Convert dictionary back to DataFrame
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pickle.load(open(os.path.join(BASE_DIR, 'similarity.pkl'), 'rb'))

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    movie_list = sorted(
        list(enumerate(distances)), 
        reverse=True, 
        key=lambda x: x[1]
    )[1:6]

    recommended_names = []
    recommended_posters = []

    for i in movie_list:
        movie_title = movies.iloc[i[0]].title
        recommended_names.append(movie_title)

        # Convert title to filename format
        poster_filename = movie_title.lower().replace(" ", "_").replace(":", "") + ".jpg"
        poster_path = os.path.join("posters", poster_filename)

        # If poster not found, show placeholder
        if os.path.exists(poster_path):
            recommended_posters.append(poster_path)
        else:
            recommended_posters.append("https://via.placeholder.com/300x450?text=No+Image")

    return recommended_names, recommended_posters
def get_movie_details(movie_title):
    movie_row = movies[movies['title'] == movie_title].iloc[0]
    overview = movie_row['overview']
    rating = movie_row['vote_average']
    return overview, rating

# ---------------- APP UI ----------------
st.markdown("<h1> 🎬 Movie Recommender</h1>", unsafe_allow_html=True)

selected_movie = st.selectbox(
    "🎥 Choose a movie",
    movies['title'].values
)

if st.button("Recommend", key="recommend_btn"):

    recommended_names, recommended_posters = recommend(selected_movie)

    st.markdown("## 🔥 Recommended For You")

    cols = st.columns(5)

    for i in range(len(recommended_names)):
        with cols[i]:

            # 🎬 Poster
            st.image(recommended_posters[i], width=220)

            # 🎥 Movie title
            st.markdown(
                f"""
                <div style="
                    color: white;
                    text-align: center;
                    font-weight: 600;
                    font-size: 17px;
                    margin-top: 8px;
                ">
                    {recommended_names[i]}
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # ▶ Watch Trailer
            trailer_url = TRAILERS.get(recommended_names[i])

            if trailer_url:
                with st.expander("▶ Watch Trailer"):
                  st.video(trailer_url)
            else:
                st.caption("Trailer not available")


# ---------------- FOOTER ----------------
st.markdown(
    "<p style='font-size:12px; color:gray; text-align:center;'>"
    "Movie recommendation system built using Machine Learning (Cosine Similarity).</p>",
    unsafe_allow_html=True
)