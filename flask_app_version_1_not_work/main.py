from flask import Flask, render_template, request, jsonify
from great_functions import random_leetcodetest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    form_data = request.form
    # Perform prediction using your functions
    result = random_leetcodetest(form_data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
