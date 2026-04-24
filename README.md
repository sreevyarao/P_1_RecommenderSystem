![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

🎬 Movie Recommender System (FILMFLIX)
<br>
A Machine Learning-based movie recommendation system built using Content-Based Filtering and Cosine Similarity, with an interactive Netflix-style UI using Streamlit.



🚀 Features

* Recommends top 5 similar movies
* Displays movie posters
* Shows trailers (YouTube integration)
* Interactive UI using Streamlit
* Fast similarity-based recommendations



🧠 How It Works

* Movie data is processed and combined into tags
* Text is converted into vectors using Count Vectorizer
* Cosine Similarity is used to find similar movies
* Top 5 recommendations are displayed



🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Pickle


📂 Project Structure

movie.py → Main Streamlit app
model.py → Model building script
posters/ → Movie poster images
similarity.pkl → Similarity matrix (not included due to size)


⚠️ Note

The file similarity.pkl is not included due to GitHub size limits.
Run model.py to generate it locally.



▶️ Run Locally

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run movie.py
```


📸 Output

screenshots/Intro Screen.png
<br>
screenshots/main page(movie selection & recommendations).png
<br>
screenshots/final page(poster+trailers).png


🎥 Demo Video
https://youtu.be/Fp1ctRTAKZQ


🌟 Future Improvements
Add Telugu/Hindi movie dataset
Use TMDB API for dynamic posters
Add user login & personalization
Deploy online (Streamlit Cloud)


👩‍💻 Author

Sreevya Rao
B.Tech CSE (AI & ML)
