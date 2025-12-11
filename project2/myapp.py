import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"
data = {  
    "id":'1',
    "name":'Farooq',
    "age":'24',
    "city":'Lahore',
    "roll":'4407'
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)