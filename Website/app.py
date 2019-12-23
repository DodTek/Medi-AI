import numpy as np
from flask import Flask, request, jsonify, render_template, url_for, session, redirect
from flask_pymongo import PyMongo
#import pickle as p
import os
import keras
import bcrypt
import json
import requests

app = Flask(__name__)
app.secret_key = 'mysecret'
basepath = os.path.abspath(".")

app.config['MONGO_DBNAME'] = 'mediweb'
app.config['MONGO_URI'] = 'mongodb+srv://root:root@mediaiprojectmp-hi8ca.mongodb.net/mediweb?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        phone_users = mongo.db.phone_users
        diabetes = mongo.db.diabetes.find()
        cancer = mongo.db.cancer.find()
        heart_disease = mongo.db.heart_disease.find()
        doctor_patients = phone_users.find({'doctor_name' : session['username']})
        return render_template('homepage.html', username_text=session['username'], patients_collection=doctor_patients, diabetes_collection = diabetes, cancer_collection = cancer, heartdisease_collection = heart_disease)
    return render_template('index.html')

@app.route('/patient_details')
def patient_details():
    if 'username' in session:
        phone_users = mongo.db.phone_users
        doctor_patients = phone_users.find({'doctor_name' : session['username']})
        return render_template('patient_details.html', username_text=session['username'], patients_collection=doctor_patients)
    return render_template('index.html')

@app.route('/patient_details/<string:email>', methods=['POST', 'GET'])
def patient_details_display(email):
    if 'username' in session:
        phone_users = mongo.db.phone_users
        patient_info = phone_users.find_one({'email' : email})
        diabetes_info = mongo.db.diabetes.find_one({'user_email' : email})
        cancer_info = mongo.db.cancer.find_one({'user_email' : email})
        heart_disease_info = mongo.db.heart_disease.find_one({'user_email' : email})
        return render_template('patient_details_display.html', username_text=session['username'], patient=patient_info, diabetes=diabetes_info, cancer=cancer_info, heart_disease=heart_disease_info)
    return render_template('index.html')

@app.route('/graphs')
def graphs():
    if 'username' in session:
        yesDiabetes = mongo.db.diabetes.count({'prediction' : 1})
        noDiabetes = mongo.db.diabetes.count({'prediction' : 0})
        yesCancer = mongo.db.cancer.count({'prediction' : 1})
        noCancer = mongo.db.cancer.count({'prediction' : 0})
        yesHeartDisease = mongo.db.heart_disease.count({'prediction' : 1})
        noHeartDisease = mongo.db.heart_disease.count({'prediction' : 0})
        return render_template('graphs.html', username_text=session['username'], yesDiabetesAmount=yesDiabetes, noDiabetesAmount=noDiabetes, yesCancerAmount=yesCancer, noCancerAmount=noCancer, yesHeartDiseaseAmount=yesHeartDisease, noHeartDiseaseAmount=noHeartDisease)
    return render_template('index.html')

@app.route('/add_users')
def add_patient_details():
    if 'username' in session:
        return render_template('add_patient_details.html', username_text=session['username'])
    return render_template('index.html')

@app.route('/add_users/add_patient', methods=['POST', 'GET'])
def add_patient():
    if 'username' in session:
        if request.method == 'POST':
            mongo.db.phone_users.insert({'first_name' : request.form['first_name'], 'surname' : request.form['surname'], 'email' : request.form['email'], 'password' : 'default', 'doctor_name' : session['username']})
            return render_template('finished_adding.html', username_text=session['username'])
        return render_template('add_patient.html', username_text=session['username'])
    return render_template('index.html')

@app.route('/add_users/predict_diabetes', methods=['POST', 'GET'])
def predict_diabetes():
    if 'username' in session:
        if request.method == 'POST':
            toPost = {'user_email': request.form['user_email'], 'Pregnancies': request.form['pregnancies'], 'Glucose': request.form['glucose'], 'BloodPressure': request.form['blood_pressure'], 'SkinThickness': request.form['skin_thickness'], 'Insulin': request.form['insulin'], 'BMI': request.form['bmi'], 'DiabetesPedigreeFunction': request.form['pedigree_function'], 'AgeYears': request.form['age']}
            url = 'http://mp00152561.pythonanywhere.com/diabetes_api'
            jd = json.dumps(toPost)
            r = requests.post(url, json=jd)
            n = r.json()
            return render_template('predict_diabetes.html', username_text=session['username'], prediction_result = 'Prediction: '+n.get('prediction'))
        return render_template('predict_diabetes.html', username_text=session['username'])
    return render_template('index.html')

@app.route('/add_users/predict_cancer', methods=['POST', 'GET'])
def predict_cancer():
    if 'username' in session:
        if request.method == 'POST':
            toPost = {'user_email': request.form['user_email'], 'Age': request.form['age'], 'BMI': request.form['bmi'], 'Glucose': request.form['glucose'], 'Insulin': request.form['insulin'], 'HOMA': request.form['homa'], 'Leptin': request.form['leptin'], 'Adiponectin': request.form['adiponectin'], 'Resistin': request.form['sesistin'], 'MCP-1': request.form['mcp']}
            url = 'http://mp00152561.pythonanywhere.com/cancer_api'
            jd = json.dumps(toPost)
            r = requests.post(url, json=jd)
            n = r.json()
            return render_template('predict_cancer.html', username_text=session['username'], prediction_result = 'Prediction: '+n.get('prediction'))
        return render_template('predict_cancer.html', username_text=session['username'])
    return render_template('index.html')

@app.route('/add_users/predict_heart_disease', methods=['POST', 'GET'])
def predict_heart_disease():
    if 'username' in session:
        if request.method == 'POST':
            toPost = {'user_email': request.form['user_email'], 'age': request.form['age'], 'sex': request.form['sex'], 'cp': request.form['cp'], 'trestbps': request.form['trestbps'], 'chol': request.form['chol'], 'fbs': request.form['fbs'], 'restecg': request.form['restecg'], 'thalach': request.form['thalach'], 'exang': request.form['exang'], 'oldpeak': request.form['oldpeak'], 'slope': request.form['slope'], 'ca': request.form['ca'], 'thal': request.form['thal']}
            url = 'http://mp00152561.pythonanywhere.com/heartdisease_api'
            jd = json.dumps(toPost)
            r = requests.post(url, json=jd)
            n = r.json()
            return render_template('predict_heart_disease.html', username_text=session['username'], prediction_result = 'Prediction: '+n.get('prediction'))
        return render_template('predict_heart_disease.html', username_text=session['username'])
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'email' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = login_user['name']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            if "@" not in request.form['username']:
                return 'Invalid username, not an email.'
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'email' : request.form['username'], 'name' : request.form['name'], 'password' : hashpass})
            session['username'] = request.form['name']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/diabetes_api',methods=['POST'])
def diabetes_api():
    model = keras.models.load_model('/home/mp00152561/MediWeb/diabetesModel.h5')
    print("DIABETES API REQUESTED", flush = True)
    data = request.get_json()
    if (type(data) == str):
        data = json.loads(data)
    print("DIABETES RECEIVED:",data, flush = True)
    X = []
    Y = []
    for key in data.keys():
            Y.append(key)

    for i in range(len(data)):
        #print("i:", i, flush = True)
        if (i != 0):
            X.append(float(data[Y[i]]))

    Xpredictdataset = np.array([X])
    print("PREDICTION DATA SET:", Xpredictdataset, flush = True)
    prediction = model.predict_classes(Xpredictdataset)
    print("PREDICTION:", prediction, flush = True)
    output = {'prediction' : str(json.dumps(prediction[0][0].tolist()))}
    data["prediction"] = str(prediction[0][0].tolist())
    print("DICTIONARY:", data, flush = True)

    diabetes = mongo.db.diabetes
    diabetes_user = diabetes.find_one({'user_email' : data["user_email"]})

    if (diabetes_user):
        diabetes.delete_one({'user_email' : data["user_email"]})
        diabetes.insert(data)
    else:
        diabetes.insert(data)

    print("API FULLY COMPLETED", flush = True)
    return jsonify(output)

@app.route('/cancer_api',methods=['POST'])
def cancer_api():
    model = keras.models.load_model('/home/mp00152561/MediWeb/cancerModel.h5')
    print("CANCER API REQUESTED", flush = True)
    data = request.get_json()
    print("data type:", type(data), flush = True)
    print("data:", data, flush = True)
    if (type(data) == str):
        data = json.loads(data)
    print("data:", type(data), flush = True)
    X = []
    Y = []
    for key in data.keys():
        #print("key:", key, flush = True)
        Y.append(key)

    for i in range(len(data)):
        #print("i:", i, flush = True)
        if (i != 0):
            X.append(float(data[Y[i]]))
    Xpredictdataset = np.array([X])
    print("PREDICTION DATA SET:", Xpredictdataset, flush = True)
    prediction = model.predict_classes(Xpredictdataset)
    print("PREDICTION:", prediction, flush = True)
    data["prediction"] = str(prediction[0][0].tolist())
    output = {'prediction' : str(json.dumps(prediction[0][0].tolist()))}
    print("DICTIONARY:", data, flush = True)

    cancer = mongo.db.cancer
    cancer_user = cancer.find_one({'user_email' : data["user_email"]})

    if (cancer_user):
        cancer.delete_one({'user_email' : data["user_email"]})
        cancer.insert(data)
    else:
        cancer.insert(data)
    print("OUTPUT:", output , flush = True)
    print("API FULLY COMPLETED", flush = True)
    return jsonify(output)

@app.route('/heartdisease_api',methods=['POST'])
def heartdisease_api():
    model = keras.models.load_model('/home/mp00152561/MediWeb/heartdiseaseModel.h5')
    print("HEART DISEASE API REQUESTED", flush = True)
    data = request.get_json()
    if (type(data) == str):
        data = json.loads(data)
    X = []
    Y = []
    for key in data.keys():
            Y.append(key)

    for i in range(len(data)):
        #print("i:", i, flush = True)
        if (i != 0):
            X.append(float(data[Y[i]]))

    Xpredictdataset = np.array([X])
    print("PREDICTION DATA SET:", Xpredictdataset, flush = True)
    prediction = model.predict_classes(Xpredictdataset)
    print("PREDICTION:", prediction, flush = True)
    output = {'prediction' : str(json.dumps(prediction[0][0].tolist()))}
    data["prediction"] = str(prediction[0][0].tolist())
    print("DICTIONARY:", data, flush = True)

    heart = mongo.db.heart_disease
    heart_user = heart.find_one({'user_email' : data["user_email"]})

    if (heart_user):
        heart.delete_one({'user_email' : data["user_email"]})
        heart.insert(data)
    else:
        heart.insert(data)

    print("API FULLY COMPLETED", flush = True)
    return jsonify(output)

@app.route('/phone_login', methods=['POST'])
def phone_login():
    users = mongo.db.phone_users
    data = request.get_json()
    print("Data type:",type(data), flush = True)
    print("Data:",data, flush = True)
    login_user = users.find_one({'email' : data["email"]})

    if login_user:
        print("Username correct", flush = True)
        if data['password'] == login_user['password']:
            print("Password correct", flush = True)
            return jsonify({'login':'success'})
    print("Username/password incorrect", flush = True)
    return jsonify({'login':'failure'})

@app.route('/phone_register', methods=['POST'])
def phone_register():
    doctor = mongo.db.users
    users = mongo.db.phone_users
    data = request.get_json()
    print("data:",data,flush = True)
    existing_user = users.find_one({'email' : data["email"]})
    existing_doctor = doctor.find_one({'name' : data["doctor_name"]})

    if existing_user is None:
        if existing_doctor is None:
            return jsonify({'valid' : '1'})
        else:
            users.insert(data)
            return jsonify({'valid' : '2'})

    return jsonify({'valid' : '0'})

@app.route('/get_details', methods=['POST'])
def get_details():
    data = request.get_json()
    print("Data type:",type(data), flush = True)
    print("Data:",data, flush = True)
    diabetes_info = mongo.db.diabetes.find_one({'user_email' : data["email"]})
    cancer_info = mongo.db.cancer.find_one({'user_email' : data["email"]})
    heart_disease_info = mongo.db.heart_disease.find_one({'user_email' : data["email"]})
    diabetes_pred = ""
    cancer_pred = ""
    heart_disease_pred = ""

    if diabetes_info is None:
        diabetes_pred = 0
    else:
        diabetes_pred = diabetes_info['prediction']
    if cancer_info is None:
        cancer_pred = 0
    else:
        cancer_pred = cancer_info['prediction']
    if heart_disease_info is None:
        heart_disease_pred = 0
    else:
        heart_disease_pred = heart_disease_info['prediction']

    return jsonify({'diabetes': diabetes_pred, 'cancer' : cancer_pred, 'heart_disease' : heart_disease_pred})

@app.route('/review', methods=['POST'])
def review():
    data = request.get_json()
    print("Data type:",type(data), flush = True)
    print("Data:",data, flush = True)
    user = mongo.db.reviews.find_one({'user_email' : data["user_email"]})

    if (user):
        mongo.db.reviews.delete_one({'user_email' : data["user_email"]})
        mongo.db.reviews.insert(data)
    else:
        mongo.db.reviews.insert(data)
    return jsonify({'received': 'Review Received'})

if __name__ == "__main__":
    app.run(debug=True)