import numpy as np
from flask import Flask, request, jsonify
import pickle
import os

# Get path to file dynamically
WD = os.path.dirname(os.path.abspath(__file__))

# generate flask app object
app = Flask(__name__)
# Read pickle regression model
model = pickle.load(open(os.path.dirname(WD) + '/models/pickled/model.pkl','rb'))

# Create endpoint /predict-salary
@app.route('/predict-salary', methods=['POST', 'GET'])
def predict():
    # get argument parameter from endpoint
    data = request.args
    # Predict with regression model
    prediction = model.predict([[np.array(eval(data['exp']))]])
    # Get first index
    output = prediction[0]
    # Return prediction result
    return jsonify(output)

# Run endpoint server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
