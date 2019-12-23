"""
predicting with the model
"""
import requests
import json

url = 'http://mp00152561.pythonanywhere.com/cancer_api'

Xdict = {}


X = ["example@gmail.com", 49,23.5,70,2.707,0.467408667,8.8071,9.7024,7.99585,417.114]

Xdict["user_email"] = X[0]
Xdict["Age"] =X[1]
Xdict["BMI"] =X[2]
Xdict["Glucose"] =X[3]
Xdict["Insulin"] =X[4]
Xdict["HOMA"] =X[5]
Xdict["Leptin"] =X[6]
Xdict["Adiponectin"] =X[7]
Xdict["Resistin"] =X[8]
Xdict["MCP-1"] =X[9]

jd = json.dumps(Xdict)
print("sending:",Xdict)

r = requests.post(url,json=jd)
r.status_code
n = r.json()

print("\nprediction:",n,"of type",type(n))
print ("0 : unlikely to develop Cancer\n1 : likely to develop Cancer")