# Rock vs Mine Detection

This is a **machine learning project** that classifies underwater sonar signals to distinguish between **rocks** and **mines** using Python and Flask. It includes a trained model, a Flask API for predictions, and notebooks for experimentation.

## 📌 Features

- Binary classification of sonar signals (`R` = Rock, `M` = Mine)  
- Trained model saved as `rock_mine_model.pkl`  
- Flask web app (`app.py`) to serve predictions  
- `test_model.py` to validate model performance  
- Jupyter Notebook for data processing and model building

## 📁 Project Structure

```

.
├── .vscode/
├── ml_env/                 # Python environment (ignored)
├── New folder/
│   ├── Copy of sonar data.csv
│   └── Rock_vs_Mine_Prediction.ipynb
├── static/
├── templates/
├── app.py
├── requirements.txt
├── rock_mine_model.pkl
└── test_model.py

```

## 📊 Model

The project uses machine learning to train a classifier on sonar signal data with 60 numeric features and a target label (`R` or `M`). The trained model is saved as a pickle file and used to predict new samples.

## 🧠 How it Works

1. Load sonar dataset  
2. Preprocess features and labels  
3. Train a classifier (e.g., logistic regression or other)  
4. Save the trained model  
5. Use Flask to serve predictions






