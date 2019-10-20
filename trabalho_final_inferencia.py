import joblib
import numpy as np
from flask import Flask, request, jsonify
import pandas as pd

data = pd.read_csv("data/ks-projects-201801.csv")
category_options = data['main_category'].unique().tolist()
country_options = data['country'].unique().tolist()
currency_options = data['currency'].unique().tolist()

# Carregando modelos e encoders dos atributos
model = joblib.load('models/kickstarter_classifier.joblib')
encoder = joblib.load('models/kickstarter_encoder.joblib')
goal_scaler = joblib.load('models/kickstarter_goal_scaler.joblib')
backers_scaler = joblib.load('models/kickstarter_backers_scaler.joblib')
duration_scaler = joblib.load('models/kickstarter_duration_scaler.joblib')

app = Flask(__name__)

# Exemplo de request:
# {
#     "category": "Poetry", 
#     "main_category": "Publishing", 
#     "currency": "GBP",
#     "goal": 1000.0,
#     "country": "GB",
#     "duration_days": 58,
#     "backers": 300
# }
@app.route('/predict',  methods=['GET', 'POST'])
def predict():
    content = request.get_json()
    content['goal'] = goal_scaler.transform(np.ndarray(content['goal']).reshape(-1, 1))[0]
    content['backers'] = backers_scaler.transform(np.ndarray(content['backers']).reshape(-1, 1))[0]
    content['duration_days'] = duration_scaler.transform(np.ndarray(content['duration_days']).reshape(-1, 1))[0]
    encoded = encoder.transform([content])
    result = model.predict_proba(encoded)
    return jsonify({
        'success': result[0][1],
        'failed': result[0][0]
    })

@app.route('/categories',  methods=['GET'])
def getCategoryOptions():
    return jsonify(category_options)

@app.route('/countries',  methods=['GET'])
def getCountryOptions():
    return jsonify(country_options)

@app.route('/currencies',  methods=['GET'])
def getCurrencyOptions():
    return jsonify(currency_options)

if __name__ == '__main__':
    app.run()