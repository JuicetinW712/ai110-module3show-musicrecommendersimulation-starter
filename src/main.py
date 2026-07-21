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

    profiles = {
        "Profile 1: High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.85,
            "target_valence": 0.80,
        },
        "Profile 2: Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.30,
            "target_valence": 0.50,
        },
        "Profile 3: Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "target_valence": 0.40,
        },
        "Profile 4 (Adversarial): Sad High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "sad",
            "target_energy": 0.90,
            "target_valence": 0.10,
        },
        "Profile 5 (Adversarial): High-Energy Lofi Focus": {
            "favorite_genre": "lofi",
            "favorite_mood": "focused",
            "target_energy": 0.95,
            "target_valence": 0.90,
        },
    }

    for name, prefs in profiles.items():
        print(f"\n============================================================")
        print(f" PROFILE: {name}")
        print(f" Preferences: {prefs}")
        print(f"============================================================")
        recommendations = recommend_songs(prefs, songs, k=5)
        print_recommendations(recommendations)


if __name__ == "__main__":
    main()

