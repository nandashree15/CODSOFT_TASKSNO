import streamlit as st
import pandas as pd
import requests
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS - CINEMATIC DARK THEME
# ============================================================

st.markdown("""
<style>

/* =========================================================
   MAIN BACKGROUND
   ========================================================= */

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(112, 60, 190, 0.20), transparent 30%),
        radial-gradient(circle at 85% 15%, rgba(210, 70, 180, 0.15), transparent 30%),
        linear-gradient(135deg, #050b24 0%, #08143a 45%, #12082d 100%);
    color: #f5f5ff;
}


/* Main content width */

.block-container {
    max-width: 1400px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}


/* =========================================================
   REMOVE DEFAULT STREAMLIT ELEMENTS
   ========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* =========================================================
   MAIN TITLE
   ========================================================= */

.main-title {
    font-size: 54px;
    font-weight: 800;
    letter-spacing: -2px;
    margin-bottom: 0px;
    background: linear-gradient(
        90deg,
        #ffffff,
        #a98cff,
        #ff71d1
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 24px;
    font-weight: 600;
    color: #eeeeff;
    margin-top: 2px;
    margin-bottom: 5px;
}

.description {
    font-size: 16px;
    color: #aeb7d8;
    margin-bottom: 25px;
}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {
    font-size: 26px;
    font-weight: 750;
    color: #f5f3ff;
    margin-top: 10px;
    margin-bottom: 8px;
}


/* =========================================================
   METRIC CARDS
   ========================================================= */

[data-testid="stMetric"] {
    background: rgba(19, 31, 76, 0.72);
    border: 1px solid rgba(132, 110, 255, 0.35);
    border-radius: 16px;
    padding: 18px 20px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
}

[data-testid="stMetricLabel"] {
    color: #aeb8dd !important;
    font-size: 14px !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 28px !important;
    font-weight: 700 !important;
}


/* =========================================================
   DIVIDERS
   ========================================================= */

hr {
    border: none !important;
    border-top: 1px solid rgba(154, 143, 255, 0.22) !important;
    margin: 30px 0 !important;
}


/* =========================================================
   SEARCH AREA
   ========================================================= */

div[data-baseweb="select"] > div {
    background: rgba(17, 32, 78, 0.90) !important;
    border: 1px solid rgba(139, 117, 255, 0.55) !important;
    border-radius: 12px !important;
    color: white !important;
}

div[data-baseweb="select"] span {
    color: #f5f5ff !important;
}

div[data-baseweb="select"] input {
    color: white !important;
}


/* =========================================================
   SELECTED MOVIE BOX
   ========================================================= */

.selected-box {
    background: linear-gradient(
        90deg,
        rgba(70, 55, 170, 0.65),
        rgba(137, 50, 175, 0.55)
    );
    border: 1px solid rgba(161, 126, 255, 0.65);
    border-radius: 14px;
    padding: 15px 20px;
    margin-top: 15px;
    margin-bottom: 20px;
    color: #ffffff;
    box-shadow: 0 8px 25px rgba(78, 42, 150, 0.25);
}


/* =========================================================
   BUTTON
   ========================================================= */

.stButton > button {
    background: linear-gradient(
        90deg,
        #7654ff,
        #d34fca
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 12px !important;

    padding: 12px 25px !important;

    font-size: 16px !important;
    font-weight: 700 !important;

    box-shadow:
        0 8px 25px rgba(122, 76, 255, 0.35);

    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 12px 30px rgba(205, 76, 220, 0.45);
}


/* =========================================================
   RECOMMENDATION CARD
   ========================================================= */

.movie-card {
    background:
        linear-gradient(
            135deg,
            rgba(17, 32, 78, 0.94),
            rgba(25, 17, 63, 0.94)
        );

    border: 1px solid rgba(133, 115, 255, 0.32);

    border-radius: 18px;

    padding: 20px;

    margin-bottom: 20px;

    box-shadow:
        0 10px 35px rgba(0, 0, 0, 0.28);

    transition: all 0.25s ease;
}

.movie-card:hover {
    border-color: rgba(186, 140, 255, 0.65);
    transform: translateY(-2px);
}


/* Movie title */

.movie-title {
    font-size: 25px;
    font-weight: 750;
    color: #ffffff;
    margin-bottom: 12px;
}


/* Movie information */

.movie-info {
    font-size: 15px;
    line-height: 1.7;
    color: #d1d6ee;
}


/* Similarity */

.similarity {
    display: inline-block;

    background: rgba(117, 83, 255, 0.18);

    border: 1px solid rgba(140, 112, 255, 0.35);

    border-radius: 8px;

    padding: 5px 10px;

    color: #c9b8ff;

    font-size: 14px;
    font-weight: 700;

    margin-top: 8px;
}


/* =========================================================
   POSTERS
   ========================================================= */

img {
    border-radius: 12px;
}


/* =========================================================
   INFO BOXES
   ========================================================= */

.info-card {
    background: rgba(15, 28, 70, 0.75);
    border: 1px solid rgba(130, 115, 240, 0.28);
    border-radius: 14px;
    padding: 20px;
    min-height: 150px;
}

.info-card-title {
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
}

.info-card-text {
    font-size: 14px;
    line-height: 1.6;
    color: #b8c0df;
}


/* =========================================================
   TECHNOLOGY CARDS
   ========================================================= */

.tech-card {
    background: rgba(16, 28, 67, 0.78);
    border: 1px solid rgba(132, 113, 235, 0.28);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    color: #e9e7ff;
    font-weight: 600;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;
    color: #8f98bd;
    padding: 30px 10px 10px 10px;
    font-size: 13px;
    line-height: 1.8;
}

.footer strong {
    color: #c7b6ff;
}


/* =========================================================
   SMALL TEXT
   ========================================================= */

.small-text {
    color: #9da7cc;
    font-size: 14px;
}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 768px) {

    .main-title {
        font-size: 38px;
    }

    .subtitle {
        font-size: 20px;
    }

    .description {
        font-size: 14px;
    }

    .movie-title {
        font-size: 21px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TMDB API
# ============================================================

TMDB_API_KEY = st.secrets["TMDB_API_KEY"]

TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"


# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_data():

 movies = pd.read_csv("data/movies.csv")

    required_columns = [
        "title",
        "genres",
        "keywords",
        "overview",
        "vote_average"
    ]

    movies = movies[required_columns]

    movies["title"] = movies["title"].fillna("")
    movies["genres"] = movies["genres"].fillna("")
    movies["keywords"] = movies["keywords"].fillna("")
    movies["overview"] = movies["overview"].fillna("")
    movies["vote_average"] = movies["vote_average"].fillna(0)

    movies["combined_features"] = (
        movies["genres"].astype(str)
        + " "
        + movies["keywords"].astype(str)
        + " "
        + movies["overview"].astype(str)
    )

    return movies


movies = load_data()


# ============================================================
# TF-IDF + COSINE SIMILARITY
# ============================================================

@st.cache_resource
def create_similarity_matrix(data):

    tfidf = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = tfidf.fit_transform(
        data["combined_features"]
    )

    similarity_matrix = cosine_similarity(
        tfidf_matrix
    )

    return similarity_matrix


similarity_matrix = create_similarity_matrix(movies)


# ============================================================
# CLEAN GENRES
# ============================================================

def clean_genres(genre_value):

    if not genre_value:
        return "Genre unavailable"

    try:

        genres = json.loads(genre_value)

        if isinstance(genres, list):

            names = []

            for genre in genres:

                if isinstance(genre, dict):

                    name = genre.get("name")

                    if name:
                        names.append(name)

            if names:
                return " • ".join(names)

    except Exception:
        pass

    return str(genre_value)


# ============================================================
# GET MOVIE POSTER FROM TMDB
# ============================================================

@st.cache_data
def get_movie_poster(movie_title):

    try:

        params = {
            "api_key": TMDB_API_KEY,
            "query": movie_title,
            "language": "en-US"
        }

        response = requests.get(
            TMDB_SEARCH_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 200:

            data = response.json()

            results = data.get(
                "results",
                []
            )

            if results:

                poster_path = results[0].get(
                    "poster_path"
                )

                if poster_path:

                    return (
                        "https://image.tmdb.org/t/p/w500"
                        + poster_path
                    )

    except Exception:
        pass

    return None


# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

def recommend(movie_title):

    matches = movies[
        movies["title"].str.lower()
        == movie_title.lower()
    ]

    if matches.empty:
        return []

    movie_index = matches.index[0]

    scores = list(
        enumerate(
            similarity_matrix[movie_index]
        )
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in scores[1:11]:

        movie = movies.iloc[index]

        recommendations.append({
            "title": movie["title"],
            "genres": clean_genres(movie["genres"]),
            "rating": movie["vote_average"],
            "similarity": score,
            "overview": movie["overview"]
        })

    return recommendations


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎬 CineMatch</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Intelligent Movie Recommendation System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">'
    'Discover movies similar to the ones you love using '
    'content-based machine learning.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PROJECT STATISTICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "🎬 Movies",
        f"{len(movies):,}"
    )

with col2:

    st.metric(
        "⚙️ Method",
        "Content-Based"
    )

with col3:

    st.metric(
        "🧠 ML Model",
        "TF-IDF"
    )

with col4:

    st.metric(
        "📊 Similarity",
        "Cosine"
    )


st.divider()


# ============================================================
# MOVIE SEARCH
# ============================================================

st.markdown(
    '<div class="section-title">🔎 Find a Movie</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="small-text">'
    'Type a movie name to search, or click the dropdown arrow '
    'to browse the available movies.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


movie_list = (
    movies["title"]
    .dropna()
    .drop_duplicates()
    .sort_values()
    .tolist()
)


selected_movie = st.selectbox(
    "Search or choose a movie",
    movie_list,
    index=None,
    placeholder="Start typing a movie name...",
    key="movie_selector"
)


# ============================================================
# SELECTED MOVIE INFORMATION
# ============================================================

if selected_movie:

    selected_data = movies[
        movies["title"] == selected_movie
    ]

    if not selected_data.empty:

        selected_movie_data = selected_data.iloc[0]

        selected_genres = clean_genres(
            selected_movie_data["genres"]
        )

        st.markdown(
            f"""
            <div class="selected-box">
                🎬 <strong>Selected:</strong> {selected_movie}
                &nbsp;&nbsp; | &nbsp;&nbsp;
                ⭐ <strong>Rating:</strong>
                {selected_movie_data['vote_average']:.1f}/10
                &nbsp;&nbsp; | &nbsp;&nbsp;
                🎭 <strong>Genres:</strong> {selected_genres}
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# RECOMMENDATION BUTTON
# ============================================================

st.write("")

button_col1, button_col2, button_col3 = st.columns(
    [1, 2, 1]
)

with button_col2:

    get_recommendations = st.button(
        "✨ Get Recommendations",
        use_container_width=True,
        key="recommend_button"
    )


# ============================================================
# RECOMMENDATIONS
# ============================================================

if get_recommendations:

    if not selected_movie:

        st.warning(
            "Please search for or select a movie first."
        )

    else:

        with st.spinner(
            "🤖 Finding movies you may like..."
        ):

            recommendations = recommend(
                selected_movie
            )

        if recommendations:

            st.divider()

            st.markdown(
                '<div class="section-title">'
                '🎬 Recommended Movies'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="small-text">
                Because you selected <strong>{selected_movie}</strong>,
                CineMatch found these movies based on similar content.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            # Display recommendations

            for number, movie in enumerate(
                recommendations,
                1
            ):

                poster_url = get_movie_poster(
                    movie["title"]
                )

                st.markdown(
                    '<div class="movie-card">',
                    unsafe_allow_html=True
                )

                poster_col, info_col = st.columns(
                    [1, 3]
                )

                # Poster

                with poster_col:

                    if poster_url:

                        st.image(
                            poster_url,
                            width=210
                        )

                    else:

                        st.info(
                            "Poster unavailable"
                        )

                # Movie information

                with info_col:

                    st.markdown(
                        f"""
                        <div class="movie-title">
                            {number}. {movie["title"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"""
                        <div class="movie-info">
                            ⭐ <strong>Rating:</strong>
                            {movie["rating"]:.1f}/10
                            <br>
                            🎭 <strong>Genres:</strong>
                            {movie["genres"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"""
                        <div class="similarity">
                            📊 Content Similarity:
                            {movie["similarity"] * 100:.1f}%
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.write("")

                    st.markdown(
                        "📝 **Overview**"
                    )

                    if movie["overview"]:

                        st.write(
                            movie["overview"]
                        )

                    else:

                        st.write(
                            "No description available."
                        )

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


# ============================================================
# HOW IT WORKS
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">'
    '🧠 How CineMatch Works'
    '</div>',
    unsafe_allow_html=True
)

step1, step2, step3 = st.columns(3)


with step1:

    st.markdown(
        """
        <div class="info-card">
            <div class="info-card-title">
                🎬 1. Movie Features
            </div>
            <div class="info-card-text">
                The system uses movie information such as
                genres, keywords and descriptions to understand
                the content of each movie.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with step2:

    st.markdown(
        """
        <div class="info-card">
            <div class="info-card-title">
                🧠 2. TF-IDF
            </div>
            <div class="info-card-text">
                TF-IDF converts movie descriptions into
                numerical feature vectors that can be
                processed by the recommendation model.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with step3:

    st.markdown(
        """
        <div class="info-card">
            <div class="info-card-title">
                📊 3. Similarity
            </div>
            <div class="info-card-text">
                Cosine similarity compares the movie vectors
                and identifies movies with similar content.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.write("")

st.markdown(
    '<div class="section-title">'
    '🛠️ Technology Stack'
    '</div>',
    unsafe_allow_html=True
)

tech1, tech2, tech3, tech4, tech5 = st.columns(5)


with tech1:

    st.markdown(
        '<div class="tech-card">🐍<br>Python</div>',
        unsafe_allow_html=True
    )


with tech2:

    st.markdown(
        '<div class="tech-card">🐼<br>Pandas</div>',
        unsafe_allow_html=True
    )


with tech3:

    st.markdown(
        '<div class="tech-card">🧠<br>Scikit-learn</div>',
        unsafe_allow_html=True
    )


with tech4:

    st.markdown(
        '<div class="tech-card">🌐<br>Streamlit</div>',
        unsafe_allow_html=True
    )


with tech5:

    st.markdown(
        '<div class="tech-card">🎬<br>TMDB API</div>',
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        🎬 <strong>CineMatch</strong>
        — Content-Based Movie Recommendation System
        <br>
        Built with Python, Machine Learning and Streamlit
        <br>
        Movie data and images provided by TMDB.
    </div>
    """,
    unsafe_allow_html=True
)
