![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

# 🎬 FILMFLIX – Movie Recommendation System

A Machine Learning-powered Movie Recommendation System built using Content-Based Filtering,Count Vectorization, and Cosine Similarity to generate personalized movie recommendations.
<br>

The application features a Netflix-inspired user interface developed with Streamlit and provides movie recommendations along with posters and trailer previews.


## 📌 Project Overview

Recommendation systems power modern platforms such as Netflix, Amazon, Spotify, and YouTube by helping users discover relevant content.

This project implements a Content-Based Recommendation Engine that analyzes movie metadata and identifies movies with similar characteristics. When a user selects a movie, the system recommends the most relevant alternatives based on textual similarity.

The project demonstrates core Machine Learning concepts including:

* Data Preprocessing
* Feature Engineering
* Natural Language Processing (NLP)
* Vectorization Techniques
* Similarity Measurement
* Recommendation Systems
* Interactive ML Application Development


## 🚀 Features

✅ Recommend Top 5 Similar Movies

✅ Interactive Netflix-Style User Interface

✅ Movie Poster Display

✅ Trailer Integration

✅ Fast Similarity-Based Recommendations

✅ Offline Recommendation Generation

✅ Streamlit-Powered Web Application


## 🧠 Machine Learning Concepts Used
**Content-Based Filtering**

The recommendation engine suggests movies based on similarity between movie attributes rather than user ratings.

**Feature Engineering**

Important movie information including:

* Genres
* Keywords
* Cast
* Crew

is combined into a unified textual representation called tags.

**Count Vectorization**

Movie metadata is converted into numerical feature vectors using Count Vectorizer, which represents each movie based on the occurrence of important words and features. These vectors serve as the foundation for calculating content similarity and generating recommendations.


**Cosine Similarity**

Cosine Similarity is used to measure how closely related two movies are based on their vector representations.

Movies with higher similarity scores are recommended to the user.


## ⚙️ System Workflow

1. Load movie dataset.
2. Perform preprocessing and cleaning.
3. Combine relevant metadata into tags.
4. Convert text into numerical vectors.
5. Compute similarity matrix.
6. Select user movie input.
7. Retrieve top similar movies.
8. Display recommendations, posters, and trailers.


## 🛠️ Tech Stack
**Programming Language**

* Python
  
**Libraries & Frameworks**
  
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
  
**Machine Learning Techniques**
* Content-Based Filtering
* TF-IDF Vectorization
* Cosine Similarity


## 📂 Project Structure

```text
FILMFLIX/
│
├── movie.py                 # Main Streamlit Application
├── model.py                 # Recommendation Model Creation
├── movies.pkl               # Processed Movie Dataset
├── similarity.pkl           # Similarity Matrix (Generated Locally)
├── posters/                 # Movie Poster Assets
├── screenshots/             # Application Screenshots
├── requirements.txt         # Project Dependencies
└── README.md
```

**📊 Dataset**

The project uses movie metadata containing:

* Movie Titles
* Genres
* Keywords
* Cast Information
* Crew Information

The recommendation engine utilizes approximately 5,000 movie records for generating recommendations.

## ▶️ Running the Project Locally
### Clone Repository
```text
git clone https://github.com/sreevyarao/P_1_RecommenderSystem.git

cd P_1_RecommenderSystem
```
**Install Dependencies**
```text
pip install -r requirements.txt
```
**Generate Similarity Matrix**
```text
python model.py
```
**Launch Application**
```text
streamlit run movie.py
```
**⚠️ Note**

The file similarity.pkl is not included due to GitHub size limits.
```text
- Run model.py to generate it locally.
```


## 📸 Application Screenshots

**Home Screen**

Displays movie selection interface and recommendation controls.

screenshots/Intro Screen.png

**Recommendation Screen**

Generates personalized movie recommendations.

screenshots/main page(movie selection & recommendations).png

**Movie Details Screen**

Displays posters and trailer previews.

screenshots/final page(poster+trailers).png

## 🎥 Project Demonstration

Demo Video:
https://youtu.be/Fp1ctRTAKZQ


## 📈 Key Learning Outcomes

Through this project, I gained hands-on experience with:

* Recommendation System Design
* Machine Learning Pipelines
* Feature Engineering
* Data Preprocessing
* Vector Space Models
* Similarity Metrics
* Streamlit Application Development
* Model Integration into Real Applications


## 🌟 Future Scope
**Hybrid Recommendation System**

Upgrade the current recommendation engine into a Hybrid Recommendation System by combining:

Content-Based Filtering
Collaborative Filtering

This would improve recommendation quality by incorporating both movie characteristics and user behavior patterns.

**Personalized User Profiles**

Implement user authentication and recommendation history tracking to provide customized recommendations.

**TMDB API Integration**

Fetch:

* Dynamic Posters
* Ratings
* Reviews
* Trending Movies
* Additional Metadata

in real time.

**Regional Language Support**

Expand recommendations to:

* Telugu Movies
* Hindi Movies
* Tamil Movies
* Other Regional Cinema

**Recommendation Evaluation**

Add recommendation quality metrics such as:

* Precision@K
* Recall@K
* NDCG

for systematic model evaluation.



## Cloud Deployment

Deploy the application using Streamlit Cloud and integrate scalable backend services.



## 👨‍💻 Author

**Sarode Sreevya Rao**

B.Tech – Computer Science & Engineering (AI & Machine Learning)

**GitHub:**
https://github.com/sreevyarao

**LinkedIn:**
https://linkedin.com/in/s-sreevya-rao-79b8b9323

**Portfolio:**
https://sreevyarao.github.io/Portfolio-website

## 
⭐ If you found this project interesting, consider giving it a star.
