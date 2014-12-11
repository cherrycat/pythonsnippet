import json
from pprint import pprint
import os

os.system("curl www.reddit.com/hot.json > curledfile")
json_data=open('curledfile')
dataset = json.load(json_data)

for i in range(0,10):
    pprint (dataset["data"]["children"][i]["data"]["url"])

json_data.close()
