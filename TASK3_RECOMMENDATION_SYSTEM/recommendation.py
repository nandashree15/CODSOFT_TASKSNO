import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------------
# 1. Load the movie dataset
# -----------------------------------

movies = pd.read_csv("data/movies.csv")

# Keep only the columns we need
movies = movies[["title", "genres", "keywords", "overview", "vote_average"]]

# Replace missing values with empty text
movies["genres"] = movies["genres"].fillna("")
movies["keywords"] = movies["keywords"].fillna("")
movies["overview"] = movies["overview"].fillna("")

# -----------------------------------
# 2. Combine movie features
# -----------------------------------

movies["combined_features"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["overview"]
)

# -----------------------------------
# 3. Convert text into numerical vectors
# -----------------------------------

tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(movies["combined_features"])

# -----------------------------------
# 4. Calculate similarity
# -----------------------------------

similarity = cosine_similarity(tfidf_matrix)

# -----------------------------------
# 5. Recommendation function
# -----------------------------------

def recommend(movie_title, number_of_recommendations=10):

    # Find the movie
    movie_matches = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    if movie_matches.empty:
        print("Movie not found.")
        return

    movie_index = movie_matches.index[0]

    # Get similarity scores
    similarity_scores = list(enumerate(similarity[movie_index]))

    # Sort by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print(f"\nRecommendations for: {movies.iloc[movie_index]['title']}")
    print("-" * 50)

    count = 0

    for index, score in similarity_scores[1:]:
        print(
            f"{count + 1}. "
            f"{movies.iloc[index]['title']} "
            f"(Similarity: {score:.2f}, "
            f"Rating: {movies.iloc[index]['vote_average']})"
        )

        count += 1

        if count >= number_of_recommendations:
            break


# -----------------------------------
# 6. Test the recommendation system
# -----------------------------------

if __name__ == "__main__":

    movie = input("Enter a movie you like: ")

    recommend(movie)