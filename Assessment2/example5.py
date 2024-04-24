import json


with open('ex5.json', 'r') as file:
    example = json.load(file)


for item in example:
    
    if item["name"] == "Old Fashioned" and item["type"] == "donut" and item["id"] == "0003":
        
        item["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break  


with open('ex5.json', 'w') as file:
    json.dump(example, file, indent=2)
