import json

import requests

URL = "http://127.0.0.1:8000/student/create/"

data = {
   'name': 'Shanzy',
   'role': 101, 
   'city': 'Farooqabad'

}

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)

data = r.json()
print(data)