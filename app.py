# .\ml_env\Scripts\activate

# from flask import Flask, request, jsonify, render_template
# import numpy as np
# import pickle

# app = Flask(__name__)

# # load trained model
# with open('rock_mine_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.form['features']  # comma-separated string
#         features = np.array([float(x) for x in data.split(',')]).reshape(1, -1)
#         prediction = model.predict(features)[0]
#         output = "Rock" if prediction == 'R' else "Mine"
#         return render_template('index.html', prediction_text=f"Predicted Object: {output}")
#     except Exception as e:
#         return render_template('index.html', prediction_text=f"Error: {e}")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# ✅ Load your trained model correctly
model = pickle.load(open('rock_mine_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        features = [float(x) for x in request.form['features'].split(',')]
        features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]

        # Convert model output into readable form
        result = "Rock" if prediction == 'R' else "Mine"
        return result

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
