# json.py

import json

# Sample Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "JavaScript"]
}

# Convert Python to JSON string
json_string = json.dumps(data, indent=4)
print("JSON string:")
print(json_string)

# Parse JSON string
parsed_data = json.loads(json_string)
print("\nParsed name:", parsed_data["name"])

# Write JSON to file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON from file
with open("output.json", "r") as file:
    loaded_data = json.load(file)
    print("\nLoaded from file:", loaded_data)