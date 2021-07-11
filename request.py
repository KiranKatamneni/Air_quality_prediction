import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'PM2.5':66,'PM10':118,'NO':16,'NO2':15,'NH3':23,'CO':1,'SO2':30,'O3':50})

print(r.json())