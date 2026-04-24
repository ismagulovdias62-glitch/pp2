import json

data = {
    "name": "Dias",
    "age": 17
}

json_string = json.dumps(data)

print(json_string)