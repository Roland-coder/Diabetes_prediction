from flask import Flask, request, jsonify
import util
app = Flask(__name__)



@app.route('/hello')
def hello():
    return "HI"


@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():

    pregnancies = int(request.form['pregnancies'])
    glucose = int(request.form['glucose'])
    bloodpressure = int(request.form['bloodpressure'])
    skinthickness = int(request.form['skinthickness'])
    insulin = int(request.form['insulin'])
    bmi = float(request.form['bmi'])
    diabetespedigreefunction = float(request.form['diabetespedigreefunction'])
    age = int(request.form['age'])

    response = jsonify({
        'get_diabetes' : util.get_diabetes(pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Diabetes Prediction....")
    app.run()