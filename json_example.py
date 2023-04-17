import json
json_string = '{"name":"Mikko", "ikä": 48}'
data = json.loads(json_string)
print(data)