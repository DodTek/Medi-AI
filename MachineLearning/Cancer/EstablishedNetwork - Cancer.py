"""
predicting with the model
"""
import requests
import json

url = 'http://mp00152561.pythonanywhere.com/cancer_api'

Xdict = {}


X = [48,23.5,70,2.707,0.467408667,8.8071,9.7024,7.99585,417.114]

Xdict["Age"] =X[0]
Xdict["BMI"] =X[1]
Xdict["Glucose"] =X[2]
Xdict["Insulin"] =X[3]
Xdict["HOMA"] =X[4]
Xdict["Leptin"] =X[5]
Xdict["Adiponectin"] =X[6]
Xdict["Resistin"] =X[7]
Xdict["MCP-1"] =X[8]

jd = json.dumps(Xdict)

r = requests.post(url,json=jd)
r.status_code
n = r.json()
n = n[0][0]

print(n)