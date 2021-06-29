
# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open('/home/rishabh/Desktop/Rishabh/seceon/sec2/jsonfile.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data:
    print(i['hash'])
  
# Closing file
f.close()