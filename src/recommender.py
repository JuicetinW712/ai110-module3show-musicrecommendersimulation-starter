from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_valence: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                song = {
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "valence": float(row["valence"]),
                }
            except (KeyError, ValueError) as e:
                print(f"Skipping malformed row {row}: {e}")
                continue
            songs.append(song)

    print(f"Loaded {len(songs)} songs.")
    return songs

WEIGHTS = {
    "genre": 3.5,
    "mood": 2.5,
    "energy": 2.5,
    "valence": 1.5,
}

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    reasons: List[str] = []
    score = 0.0

    # --- Genre (binary match) ---
    if song["genre"] == user_prefs["favorite_genre"]:
        points = WEIGHTS["genre"]
        score += points
        reasons.append(f"genre match (+{points:.1f})")
    else:
        reasons.append(f"genre mismatch ({song['genre']} vs {user_prefs['favorite_genre']}) (+0.0)")

    # --- Mood (binary match) ---
    if song["mood"] == user_prefs["favorite_mood"]:
        points = WEIGHTS["mood"]
        score += points
        reasons.append(f"mood match (+{points:.1f})")
    else:
        reasons.append(f"mood mismatch ({song['mood']} vs {user_prefs['favorite_mood']}) (+0.0)")

    # --- Energy (distance-based) ---
    energy_diff = abs(song["energy"] - user_prefs["target_energy"])
    energy_similarity = 1.0 - energy_diff  # assumes energy is normalized 0-1
    energy_points = WEIGHTS["energy"] * energy_similarity
    score += energy_points
    if energy_diff <= 0.1:
        reasons.append(f"energy close match (+{energy_points:.1f})")
    elif energy_diff >= 0.5:
        reasons.append(f"energy mismatch (+{energy_points:.1f})")
    else:
        reasons.append(f"energy partial match (+{energy_points:.1f})")

    # --- Valence (distance-based) ---
    valence_diff = abs(song["valence"] - user_prefs["target_valence"])
    valence_similarity = 1.0 - valence_diff  # assumes valence is normalized 0-1
    valence_points = WEIGHTS["valence"] * valence_similarity
    score += valence_points
    if valence_diff <= 0.1:
        reasons.append(f"valence close match (+{valence_points:.1f})")
    elif valence_diff >= 0.5:
        reasons.append(f"valence mismatch (+{valence_points:.1f})")
    else:
        reasons.append(f"valence partial match (+{valence_points:.1f})")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda entry: entry[1], reverse=True)

    return scored_songs[:k]
