from joblib import load
import json
from flask import Flask, request, jsonify



model = load('breast_cancer_prediction_model.joblib')
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    
    req = request.get_json()
    req = json.loads(req)

    print(req)
    print(type(req))
    input_data = req['data']
    print('input data :',input_data)
    prediction = model.predict([input_data])[0]
    if prediction==1: prediction =  'Melignant'
    else: prediction =  'Benign'
    print(prediction)
    return jsonify({'output':{'cancer_type':prediction}})
        
    
@app.route('/')
def home_page():
    return 'breast cancer prediction'

if __name__=='__main__':
    app.run(host='0.0.0.0', port='3000')