import json
import pickle
import numpy as np

__data_columns = None
__model = None

def get_diabetes(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age):
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
    global __model
    with open("./artifacts/diabetes_prediction_model.pkl", 'rb') as f:
        __model = pickle.load(f)
        print("Loading saved artifacts")
    x = np.zeros(len(__data_columns))
    x[0] = pregnancies
    x[1] = glucose
    x[2] = bloodpressure
    x[3] = skinthickness
    x[4] = insulin
    x[5] = bmi
    x[6] = diabetespedigreefunction
    x[7] = age
    print("Got everything for the model prediction")
    return __model.predict([x])[0]

if __name__ == '__main__':
    print(get_diabetes(0.36655785,  0.3513236 ,  0.62181524, -0.246317  , -0.46783056,
       -0.85282072, -0.88516878,  3.09322115))