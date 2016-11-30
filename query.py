import json
from pprint import pprint

with open('Jakarta.json') as data_file:
    data = json.load(data_file)

startHour = 10
endHour = 18
location = "jakarta"
category = ["Shopping", "Museum"]
pprint(data)