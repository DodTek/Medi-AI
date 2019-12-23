"""
predicting with the model
"""
import requests
import json

url = 'http://mp00152561.pythonanywhere.com/heartdisease_api'

Xdict = {}


X = [67,1,4,160,286,0,2,108,1,1.5,2,3,3]

Xdict["age"] =X[0]
Xdict["sex"] =X[1]
Xdict["cp"] =X[2]
Xdict["trestbps"] =X[3]
Xdict["chol"] =X[4]
Xdict["fbs"] =X[5]
Xdict["restecg"] =X[6]
Xdict["thalach"] =X[7]
Xdict["exang"] =X[8]
Xdict["oldpeak"] =X[9]
Xdict["slope"] =X[10]
Xdict["ca"] =X[11]
Xdict["thal"] =X[12]

jd = json.dumps(Xdict)



r = requests.post(url,json=jd)
r.status_code
n = r.json()
n = n[0][0]

print(n)