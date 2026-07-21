# 🎵 Music Recommender Simulation - VibeFinder 1.0

## Project Summary

VibeFinder 1.0 is a content-based music recommendation engine designed to turn user preferences (favorite genre, favorite mood, target energy, and target valence) into ranked top-K song recommendations. Built using Python, it scores songs by calculating a weighted sum of metadata matching and acoustic feature distances, offering transparent, human-readable explanations for every recommendation.

---

## How The System Works

Recommendation engines create a profile of what a user likes and dislikes, then run calculations to find items that match that taste profile.

VibeFinder 1.0 uses mood, energy, valence, and genre as predictors to rank music from `data/songs.csv`. The algorithm logic works as follows:

```
For each song in data/songs.csv:
    genre_match   = 3.5 if song.genre == profile.favorite_genre else 0.0
    mood_match    = 2.5 if song.mood  == profile.favorite_mood  else 0.0
    energy_score  = (1.0 - abs(song.energy  - profile.target_energy)) * 2.5
    valence_score = (1.0 - abs(song.valence - profile.target_valence)) * 1.5

    score = genre_match + mood_match + energy_score + valence_score

Sort results by score, descending
Return top K
```

In terms of biases, genre is the most dominant predictor since it carries a weight of 3.5 points (35% of the total 10-point scale). Because genre matching is binary, closely related genres (like `pop` vs. `indie pop`) score 0 points for genre similarity.

---

## Getting Started

### Setup

1. Activate your virtual environment (if applicable):

   ```bash
   .venv\Scripts\activate         # Windows
   source .venv/bin/activate      # Mac or Linux
   ```

2. Run the recommendation evaluation runner:

   ```bash
   python -m src.main
   ```

### Running Tests

Run the unit tests with:

```bash
pytest
```

---

## Sample Recommendation Outputs (Stress Test Profiles)

Here are the terminal recommendation outputs for 5 diverse user profiles:

```text
============================================================
 PROFILE: Profile 1: High-Energy Pop
 Preferences: {'favorite_genre': 'pop', 'favorite_mood': 'happy', 'target_energy': 0.85, 'target_valence': 0.8}
============================================================

TOP RECOMMENDATIONS

#1  Sunrise City  —  Score: 9.74/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy close match (+2.4)
    • valence close match (+1.4)

#2  Gym Hero  —  Score: 7.25/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (intense vs happy) (+0.0)
    • energy close match (+2.3)
    • valence close match (+1.5)

#3  Rooftop Lights  —  Score: 6.26/10
------------------------------------------------------------
    • genre mismatch (indie pop vs pop) (+0.0)
    • mood match (+2.5)
    • energy close match (+2.3)
    • valence close match (+1.5)

#4  Golden Hour  —  Score: 6.04/10
------------------------------------------------------------
    • genre mismatch (indie pop vs pop) (+0.0)
    • mood match (+2.5)
    • energy partial match (+2.1)
    • valence close match (+1.5)

#5  Bassline Hustle  —  Score: 3.70/10
------------------------------------------------------------
    • genre mismatch (hip-hop vs pop) (+0.0)
    • mood mismatch (confident vs happy) (+0.0)
    • energy close match (+2.4)
    • valence partial match (+1.3)


============================================================
 PROFILE: Profile 2: Chill Lofi
 Preferences: {'favorite_genre': 'lofi', 'favorite_mood': 'chill', 'target_energy': 0.3, 'target_valence': 0.5}
============================================================

TOP RECOMMENDATIONS

#1  Window Fog  —  Score: 9.95/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy close match (+2.5)
    • valence close match (+1.5)

#2  Library Rain  —  Score: 9.72/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy close match (+2.4)
    • valence close match (+1.4)

#3  Midnight Coding  —  Score: 9.61/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy partial match (+2.2)
    • valence close match (+1.4)

#4  Deep Work Beats  —  Score: 7.22/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (focused vs chill) (+0.0)
    • energy close match (+2.3)
    • valence close match (+1.4)

#5  Focus Flow  —  Score: 7.12/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (focused vs chill) (+0.0)
    • energy partial match (+2.2)
    • valence close match (+1.4)


============================================================
 PROFILE: Profile 3: Deep Intense Rock
 Preferences: {'favorite_genre': 'rock', 'favorite_mood': 'intense', 'target_energy': 0.95, 'target_valence': 0.4}
============================================================

TOP RECOMMENDATIONS

#1  Storm Runner  —  Score: 9.78/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy close match (+2.4)
    • valence close match (+1.4)

#2  Overdrive  —  Score: 9.62/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy close match (+2.4)
    • valence partial match (+1.3)

#3  Gym Hero  —  Score: 5.90/10
------------------------------------------------------------
    • genre mismatch (pop vs rock) (+0.0)
    • mood match (+2.5)
    • energy close match (+2.5)
    • valence partial match (+0.9)

#4  Thunder Dome  —  Score: 3.84/10
------------------------------------------------------------
    • genre mismatch (metal vs rock) (+0.0)
    • mood mismatch (aggressive vs intense) (+0.0)
    • energy close match (+2.5)
    • valence close match (+1.4)

#5  Night Drive Loop  —  Score: 3.37/10
------------------------------------------------------------
    • genre mismatch (synthwave vs rock) (+0.0)
    • mood mismatch (moody vs intense) (+0.0)
    • energy partial match (+2.0)
    • valence close match (+1.4)


============================================================
 PROFILE: Profile 4 (Adversarial): Sad High-Energy Pop
 Preferences: {'favorite_genre': 'pop', 'favorite_mood': 'sad', 'target_energy': 0.9, 'target_valence': 0.1}
============================================================

TOP RECOMMENDATIONS

#1  Gym Hero  —  Score: 6.42/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (intense vs sad) (+0.0)
    • energy close match (+2.4)
    • valence mismatch (+0.5)

#2  Sunrise City  —  Score: 6.19/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (happy vs sad) (+0.0)
    • energy close match (+2.3)
    • valence mismatch (+0.4)

#3  Thunder Dome  —  Score: 3.54/10
------------------------------------------------------------
    • genre mismatch (metal vs pop) (+0.0)
    • mood mismatch (aggressive vs sad) (+0.0)
    • energy close match (+2.4)
    • valence partial match (+1.2)

#4  Storm Runner  —  Score: 3.41/10
------------------------------------------------------------
    • genre mismatch (rock vs pop) (+0.0)
    • mood mismatch (intense vs sad) (+0.0)
    • energy close match (+2.5)
    • valence partial match (+0.9)

#5  Overdrive  —  Score: 3.30/10
------------------------------------------------------------
    • genre mismatch (rock vs pop) (+0.0)
    • mood mismatch (intense vs sad) (+0.0)
    • energy close match (+2.5)
    • valence partial match (+0.8)


============================================================
 PROFILE: Profile 5 (Adversarial): High-Energy Lofi Focus
 Preferences: {'favorite_genre': 'lofi', 'favorite_mood': 'focused', 'target_energy': 0.95, 'target_valence': 0.9}
============================================================

TOP RECOMMENDATIONS

#1  Focus Flow  —  Score: 8.16/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy mismatch (+1.1)
    • valence partial match (+1.0)

#2  Deep Work Beats  —  Score: 7.90/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy mismatch (+1.1)
    • valence partial match (+0.8)

#3  Midnight Coding  —  Score: 5.67/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (chill vs focused) (+0.0)
    • energy mismatch (+1.2)
    • valence partial match (+1.0)

#4  Library Rain  —  Score: 5.55/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (chill vs focused) (+0.0)
    • energy mismatch (+1.0)
    • valence partial match (+1.0)

#5  Window Fog  —  Score: 5.33/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (chill vs focused) (+0.0)
    • energy mismatch (+0.9)
    • valence partial match (+0.9)
```

---

## Experiments You Tried

We tested system sensitivity by conducting a **Weight Shift Experiment**:
- **Baseline Weights**: `genre=3.5`, `mood=2.5`, `energy=2.5`, `valence=1.5`
- **Experimental Weights**: `genre=1.75`, `mood=2.5`, `energy=5.0`, `valence=1.5` (doubled energy importance, halved genre importance)

**Results & Insights**:
- For **Chill Lofi (Profile 2)**: Low-energy ambient tracks (*Spacewalk Thoughts* & *Static Dreams*) entered the top 5 (ranks #4 & #5), replacing non-chill lofi beats.
- For **High-Energy Lofi Focus (Profile 5 - Adversarial)**: High-energy pop and rock tracks (*Gym Hero*, *Sunrise City*, *Overdrive*) broke into the top recommendations, overriding low-energy lofi tracks.
- **Takeaway**: Reducing genre dominance prevents the system from forcing genre-matched tracks onto users when the audio features (energy) strongly mismatch user expectations.

---

## Limitations and Risks

- **Filter Bubbles & Rigid Genre Matching**: Exact string equality means `pop` and `indie pop` share 0 genre similarity points.
- **Dataset Imbalance**: 25% of catalog is Lofi; genres like Metal, Hip-Hop, and Classical have only 1 song each.
- **Unrepresented Moods**: Unrepresented moods like "sad" cause mood scoring to collapse to 0 for all catalog items.

---

## Reflection

For detailed evaluation findings, pairwise profile analysis, and model governance insights, see the model card:

[**Model Card**](model_card.md)
