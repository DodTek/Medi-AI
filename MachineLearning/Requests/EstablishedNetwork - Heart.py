"""
predicting with the model
"""
import requests
import json

url = 'http://mp00152561.pythonanywhere.com/heartdisease_api'

Xdict = {}


X = ["example@gmail.com",67,1,4,160,286,0,2,108,1,1.5,2,3,3]

Xdict["user_email"]= X[0]
Xdict["age"] =X[1]
Xdict["sex"] =X[2]
Xdict["cp"] =X[3]
Xdict["trestbps"] =X[4]
Xdict["chol"] =X[5]
Xdict["fbs"] =X[6]
Xdict["restecg"] =X[7]
Xdict["thalach"] =X[8]
Xdict["exang"] =X[9]
Xdict["oldpeak"] =X[10]
Xdict["slope"] =X[11]
Xdict["ca"] =X[12]
Xdict["thal"] =X[13]

jd = json.dumps(Xdict)
print("sending:",Xdict)



r = requests.post(url,json=jd)
r.status_code
n = r.json()

print("\nprediction:",n,"of type",type(n))
print ("0 : unlikely to develop heart disease\n1 : likely to develop heart disease")