
# 🎬 Movie Recommendation System  

A **content-based recommendation system** that suggests movies similar to the one selected by the user.  
Built with **Python**, **Machine Learning**, and **Streamlit**, this project demonstrates how data preprocessing, feature engineering, and cosine similarity can be combined to build a recommendation engine.  

🌐 **Live Demo:** [Click here to try it](https://movierecommandationsystem-kwuocn9krrw4jpqur2r3un.streamlit.app/)  

---

## 📖 Table of Contents


- 🚀 [About the Project](#-about-the-project)  
- ⚡ [Tech Stack](#-tech-stack)  
- 🔄 [Workflow](#-workflow)  
- 📂 [Project Structure](#-project-structure)  
- 🖥️ [How to Run Locally](#️-how-to-run-locally)  
- 🌐 [Deployment](#-deployment)  
- 📒 [Google Colab Notebook](#-google-colab-notebook)  
- 📊 [Results & Screenshots](#-results--screenshots)  
- 🤝 [Contributing](#-contributing)  
- 📜 [License](#-license)  

---

## 🚀 About the Project  
This project provides movie recommendations by analyzing metadata such as:  
- Overview  
- Genres  
- Keywords  
- Cast & Crew  

The **cosine similarity matrix** is used to measure similarity between movies.  
Results are served through a clean **Streamlit web app** where users can easily select a movie and view top recommended titles.  

---

## ⚡ Tech Stack  

- 🐍 **Python** – Core programming language  
- 🎨 **Streamlit** – Web app framework  
- 📊 **Pandas, NumPy** – Data processing & manipulation  
- 🤖 **Scikit-learn** – Vectorization & similarity computation  
- 💾 **Pickle** – Saving preprocessed data & similarity model  
- 🔗 **Git LFS** – Storing large files like `.pkl`  
- ☁️ **Streamlit Community Cloud** – Free deployment  

---

## 🔄 Workflow  

### 1️⃣ Dataset Loading  
- Loaded TMDB dataset in **Google Colab**  
- Extracted useful columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`  

### 2️⃣ Data Preprocessing  
- Removed missing values  
- Converted JSON-like fields (genres, keywords, cast, crew) into clean lists  
- Extracted top 3 cast members + director  
- Cleaned text: removed spaces, lowercase conversion, stemming  

### 3️⃣ Feature Engineering  
- Combined cleaned features into a single **tags** column  
- Used **CountVectorizer** to convert text into numeric vectors  

### 4️⃣ Similarity Computation  
- Computed **cosine similarity** across all movies  
- Saved processed data into:  
  - `movies_dict.pkl` → dictionary of movie metadata  
  - `similarity.pkl` → cosine similarity matrix  

### 5️⃣ Model Serving (Streamlit App)  
- User selects a movie from dropdown menu  
- System queries similarity matrix → fetches top 5 similar movies  
- Displays recommended titles (and posters if enabled)  

### 6️⃣ Deployment  
- Managed large `.pkl` files with **Git LFS**  
- Hosted on **Streamlit Cloud**  

---

## 📂 Project Structure  

MovieRecommandationSystem/
├── Colab_notebook.ipynb # Data preprocessing & model building
├── app.py # Streamlit application
├── movies_dict.pkl # Serialized movie dictionary
├── similarity.pkl # Precomputed similarity matrix
├── requirements.txt # Project dependencies
├── .gitattributes # Git LFS config
├── LICENSE # MIT License
└── README.md # Project documentation


---

## 🖥️ How to Run Locally  

```bash

git clone https://github.com/faryal-art/MovieRecommandationSystem.git
cd MovieRecommandationSystem
```
pip install -r requirements.txt
streamlit run app.py

## 🌐 Deployment

- Deployed on Streamlit Community Cloud:
- Push repo files (app.py, .pkl, requirements.txt)
- Go to share.streamlit.io
- Select repo → branch: master → main file: app.py
- Click Deploy 🎉

## 📒 Google Colab Notebook

- The Colab notebook contains:
- Data loading
- Preprocessing
- Feature engineering
- Similarity computation
- Model serialization

(https://colab.research.google.com/drive/19fBbf_prOxvtuMOwjrv4EyEJb0ON3J2N#scrollTo=s0kTLHChovfA)


