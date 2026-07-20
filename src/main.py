"""
Command line runner for the Music Recommender Simulation.
This file helps you quickly run and test your recommender.
You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from .recommender import load_songs, recommend_songs

def print_recommendations(recommendations) -> None:
    """
    Prints recommendations in a clean, readable terminal layout.
    """
    print("\n" + "=" * 60)
    print("TOP RECOMMENDATIONS")
    print("=" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']}  —  Score: {score:.2f}/10")
        print("-" * 60)
        for reason in explanation.split(", "):
            print(f"    • {reason}")

    print("\n" + "=" * 60 + "\n")


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_valence": 0.7,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations(recommendations)


if __name__ == "__main__":
    main()
