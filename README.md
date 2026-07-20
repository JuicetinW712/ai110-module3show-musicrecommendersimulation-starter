# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Recommendation engines create a profile of what a user likes and dislikes. It then runs calculations to find items that are similar or items liked by users with a similar profile. This is then ranked by similarity.

My recommender uses mood, energy, valence, and genre as the predictors to predict music recommendations for a user. The algorithm will look like this

For each song in catalog.csv:
    genre_match   = 1.0 if song.genre == profile.favorite_genre else 0.0
    mood_match    = 1.0 if song.mood  == profile.favorite_mood  else 0.0
    energy_score  = 1.0 - abs(song.energy  - profile.target_energy)
    valence_score = 1.0 - abs(song.valence - profile.target_valence)

    score = (0.35 * genre_match)
          + (0.25 * mood_match)
          + (0.25 * energy_score)
          + (0.15 * valence_score)

    results.append((song, score))

Sort results by score, descending
Return top K

In terms of biases, I expect genre to be the most dominant since it has the highest weight. It's possible for a song to fit the user's mood and energy but be in a genre they don't usually like and thus will not recommend it to them. Along with that it's also binary instead of a range like energy, which can cause fluctuations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded 20 songs.

============================================================
TOP RECOMMENDATIONS
============================================================

#1  Sunrise City  —  Score: 9.74/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood match (+2.5)
    • energy close match (+2.5)
    • valence partial match (+1.3)

#2  Gym Hero  —  Score: 7.07/10
------------------------------------------------------------
    • genre match (+3.5)
    • mood mismatch (intense vs happy) (+0.0)
    • energy partial match (+2.2)
    • valence close match (+1.4)

#3  Rooftop Lights  —  Score: 6.24/10
------------------------------------------------------------
    • genre mismatch (indie pop vs pop) (+0.0)
    • mood match (+2.5)
    • energy close match (+2.4)
    • valence partial match (+1.3)

#4  Golden Hour  —  Score: 6.08/10
------------------------------------------------------------
    • genre mismatch (indie pop vs pop) (+0.0)
    • mood match (+2.5)
    • energy partial match (+2.2)
    • valence close match (+1.4)

#5  Bassline Hustle  —  Score: 3.97/10
------------------------------------------------------------
    • genre mismatch (hip-hop vs pop) (+0.0)
    • mood mismatch (confident vs happy) (+0.0)
    • energy close match (+2.5)
    • valence close match (+1.5)

============================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
