# -*- coding: utf-8 -*-
"""
predicting with the model
"""
import requests
import json

url = 'http://mp00152561.pythonanywhere.com/diabetes_api'

Xdict = {}


X = ["example@gmail.com", 8,170.0,64,0,0,23.0,0.672,32.0]

Xdict["user_email"] =X[0]
Xdict["Pregnancies"] =X[1]
Xdict["Glucose"] =X[2]
Xdict["BloodPressure"] =X[3]
Xdict["SkinThickness"] =X[4]
Xdict["Insulin"] =X[5]
Xdict["BMI"] =X[6]
Xdict["DiabetesPedigreeFunction"] =X[7]
Xdict["AgeYears"] =X[8]

jd = json.dumps(Xdict)
print("sending:",Xdict)

r = requests.post(url,json=jd)
r.status_code
n = r.json()

print("\nprediction:",n,"of type",type(n))
print ("0 : unlikely to develop Diabetes\n1 : likely to develop Diabetes")