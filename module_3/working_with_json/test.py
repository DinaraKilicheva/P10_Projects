import json

computers = [
    {"id": 1234,
     "name": "lenova",
     "color": "white"
     },
    {"id": 3492,
     "name": "Asus",
     "color": "white"
     },
    {"id": 9273,
     "name": "Asus",
     "color": "red"
     }
]

json_arr = json.dumps((computers))

with open("computers.json", "w") as f:
    json.dump(computers, f)

print(type(json.loads(json_arr)[0]))

with open("computers.json") as f:
    computers=json.load(f)
