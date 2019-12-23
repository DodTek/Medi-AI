# -*- coding: utf-8 -*-
"""
predicting with the model
"""
import requests
import json

url = 'http://mp00152561.pythonanywhere.com/diabetes_api'

Xdict = {}


X = [8,183.0,64,0,0,23.0,0.672,32.0]

Xdict["pregnancies"] =X[0]
Xdict["Glucose"] =X[1]
Xdict["BloodPressure"] =X[2]
Xdict["SkinThickness"] =X[3]
Xdict["Insulin"] =X[4]
Xdict["BMI"] =X[5]
Xdict["DiabetesPedigreeFunction"] =X[6]
Xdict["AgeYears"] =X[7]

jd = json.dumps(Xdict)



r = requests.post(url,json=jd)
r.status_code
n = r.json()
n = n[0][0]

print(n)