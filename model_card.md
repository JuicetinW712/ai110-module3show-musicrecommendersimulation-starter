# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
**VibeFinder 1.0**

---

## 2. Intended Use  

VibeFinder 1.0 is a content-based music recommendation simulation designed to match user taste profiles (favorite genre, favorite mood, target energy, and target valence) against a structured song catalog. It produces ranked top-K song recommendations accompanied by feature-level score explanations. The system is designed for classroom exploration, algorithmic stress testing, and evaluating content-based filtering trade-offs.

---

## 3. How the Model Works  

VibeFinder 1.0 uses a weighted multi-attribute scoring model. For any given user profile and candidate song, the recommender calculates similarity across four key features:

1. **Genre Match (Weight = 3.5)**: A binary check. If the song's genre exactly equals the user's favorite genre, it receives +3.5 points; otherwise, +0.0 points.
2. **Mood Match (Weight = 2.5)**: A binary check. If the song's mood exactly matches the user's favorite mood, it receives +2.5 points; otherwise, +0.0 points.
3. **Energy Match (Weight = 2.5)**: A continuous similarity score based on distance: `(1.0 - |song_energy - target_energy|) * 2.5`.
4. **Valence Match (Weight = 1.5)**: A continuous similarity score based on distance: `(1.0 - |song_valence - target_valence|) * 1.5`.

The final recommendation score is the sum of these four feature points (maximum possible score of 10.0). Songs are sorted in descending order of their total score, and the top 5 are returned with bulleted explanations detailing how each sub-score was derived.

---

## 4. Data  

The recommender evaluates a catalog of 20 songs stored in `data/songs.csv`.

- **Dataset Composition**: Includes 5 Lofi tracks (25%), 2 Pop tracks, 2 Indie Pop tracks, 2 Synthwave tracks, 2 Rock tracks, 2 Jazz tracks, 2 Ambient tracks, 1 Metal track, 1 Hip-Hop track, and 1 Classical track.
- **Mood Representation**: Happy, Chill, Intense, Relaxed, Moody, Focused, Aggressive, Confident.
- **Gaps & Oversights**: The dataset lacks representation for common emotional states such as "sad" or "melancholic". Heavy music (Metal) and Hip-Hop are represented by only 1 track each, and subgenre relationships (e.g., Pop vs. Indie Pop) are treated as completely unrelated strings.

---

## 5. Strengths  

- **Predictable & Transparent**: Score explanations make it immediately clear why each song was recommended.
- **Strong Mainstream Match**: For users whose preferences align with heavily sampled genres and standard mood pairings (e.g., Lofi + Chill or Pop + Happy), top recommendations achieve near-perfect scores (~9.7–9.9/10).
- **Smooth Continuous Adjustments**: Continuous distance scoring for energy and valence prevents minor numerical differences (e.g., 0.82 vs 0.85 energy) from penalizing good recommendations heavily.

---

## 6. Limitations and Bias 

The system heavily over-prioritizes exact genre matches because the genre weight (3.5/10) accounts for 35% of the total score. This creates a severe filter bubble where closely related subgenres (like "pop" vs "indie pop") receive zero genre points, completely ignoring subgenre similarity. Additionally, dataset sparsity is a major flaw: 25% of the catalog is lofi, whereas genres like metal, hip-hop, and classical have only a single song each, preventing diverse recommendations for those listeners. Furthermore, if a user requests an unrepresented mood (such as "sad"), mood scoring drops to 0 for all songs, forcing the system to fall back entirely on genre and energy.

---

## 7. Evaluation  

We evaluated VibeFinder 1.0 across 5 distinct user profiles, including standard taste profiles and adversarial edge cases designed to challenge the scoring logic.

### Tested Profiles & Terminal Outputs

#### Profile 1: High-Energy Pop
- **Preferences**: `favorite_genre: pop`, `favorite_mood: happy`, `target_energy: 0.85`, `target_valence: 0.80`
```text
============================================================
TOP RECOMMENDATIONS
============================================================

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
```

#### Profile 2: Chill Lofi
- **Preferences**: `favorite_genre: lofi`, `favorite_mood: chill`, `target_energy: 0.30`, `target_valence: 0.50`
```text
============================================================
TOP RECOMMENDATIONS
============================================================

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
```

#### Profile 3: Deep Intense Rock
- **Preferences**: `favorite_genre: rock`, `favorite_mood: intense`, `target_energy: 0.95`, `target_valence: 0.40`
```text
============================================================
TOP RECOMMENDATIONS
============================================================

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
```

#### Profile 4 (Adversarial): Sad High-Energy Pop
- **Preferences**: `favorite_genre: pop`, `favorite_mood: sad`, `target_energy: 0.90`, `target_valence: 0.10`
```text
============================================================
TOP RECOMMENDATIONS
============================================================

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
```

#### Profile 5 (Adversarial): High-Energy Lofi Focus
- **Preferences**: `favorite_genre: lofi`, `favorite_mood: focused`, `target_energy: 0.95`, `target_valence: 0.90`
```text
============================================================
TOP RECOMMENDATIONS
============================================================

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

### Pairwise Profile Comparisons

1. **Profile 1 (High-Energy Pop) vs. Profile 2 (Chill Lofi)**:  
   Profile 1 yields high-bpm, upbeat tracks led by *Sunrise City* (9.74) and *Gym Hero* (7.25), whereas Profile 2 yields calm, ambient beats led by *Window Fog* (9.95) and *Library Rain* (9.72). The ranking completely flips because the genre match (+3.5) and low energy target (0.30 vs 0.85) pull acoustic/lofi tracks to the top while suppressing high-energy synth drums.

2. **Profile 2 (Chill Lofi) vs. Profile 3 (Deep Intense Rock)**:  
   Profile 2 yields soft lofi tracks with low energy (0.30–0.42), whereas Profile 3 yields high-distortion rock tracks like *Storm Runner* (9.78) and *Overdrive* (9.62) with energy ~0.90–0.95. Furthermore, because the catalog only contains 2 rock songs, Profile 3's ranks #3–#5 fall off sharply to pop and metal tracks, whereas Profile 2 has enough lofi songs to fill all top 5 slots.

3. **Profile 1 (High-Energy Pop) vs. Profile 4 (Sad High-Energy Pop - Adversarial)**:  
   Both profiles request Pop and high energy (~0.85–0.90), but Profile 1 requests happy mood while Profile 4 requests "sad" mood (which is missing from the catalog). Profile 1's top track *Sunrise City* (9.74) drops to #2 (6.19) for Profile 4 because of a severe valence penalty (0.84 vs 0.10 target), allowing *Gym Hero* to take #1 (6.42) due to lower valence (0.77). However, because "sad" exists on zero songs, mood match awards +0.0 across the board, demonstrating how unrepresented moods break mood-based filtering.

4. **Profile 2 (Chill Lofi) vs. Profile 5 (High-Energy Lofi Focus - Adversarial)**:  
   Both profiles request Lofi, but Profile 2 wants low energy (0.30) chill beats while Profile 5 wants extreme high energy (0.95) focused beats. For Profile 5, *Focus Flow* (8.16) and *Deep Work Beats* (7.90) rank highest among lofi songs due to mood match, but all lofi tracks suffer an energy penalty (-1.4 pts) because no high-energy lofi track exists in the catalog. Under experimental weights (Energy 5.0, Genre 1.75), high-energy pop/rock tracks actually surpassed lofi tracks for Profile 5, revealing how genre weight can force inaccurate recommendations when catalog audio features conflict with requested genres.

### Data Experiment Results (Weight Shift)

We conducted an experiment in `recommender.py` by doubling the importance of energy (2.5 → 5.0) and halving the importance of genre (3.5 → 1.75):
- **Observation for Profile 2 (Chill Lofi)**: Low-energy ambient tracks (*Spacewalk Thoughts* and *Static Dreams*) broke into the top 5 (ranks #4 and #5), displacing non-chill lofi beats. This improved recommendation quality because chill ambient tracks sound far more similar to chill lofi than fast study beats do.
- **Observation for Profile 5 (High-Energy Lofi Focus)**: High-energy pop and rock tracks (*Gym Hero*, *Sunrise City*, *Overdrive*) broke into ranks #3, #4, and #5, bypassing low-energy lofi beats. This showed that reducing genre dominance allows audio feature matching (energy) to override misleading genre tags.

---

## 8. Future Work  

- **Subgenre Distance Matrix**: Replace exact string equality for genres with a similarity graph or embedding space (e.g., pop and indie pop having 0.8 similarity).
- **Expanded Catalog & Dynamic Mood Mapping**: Add more diverse songs across underrepresented genres (metal, hip-hop) and implement mood fallbacks (e.g., mapping "sad" to low valence + low energy).
- **Collaborative Filtering Integration**: Hybridize content scoring with user interaction history to avoid purely static rule-based limitations.

---

## 9. Personal Reflection  

Building and evaluating VibeFinder 1.0 demonstrated how easily rule-based recommendation systems can form filter bubbles and produce misleading results when datasets are imbalanced. Prior to stress testing, giving genre the highest weight seemed logical; however, adversarial testing proved that high genre weights can force a system to recommend low-energy beats to a user seeking high-energy music simply because the genre label matched. Designing effective recommenders requires constantly balancing metadata rules against continuous acoustic features.
