# program to read json file
import json

print('-----------------First Part---------------------------')

# opening json file
f = open('employee.json', 'r')

# return json object as dictionary
data = json.loads(f.read())

# iteration through the json list
for i in data['employee']:
    print(i)

# closing file
f.close()

print('-----------------Second Part---------------------------')

# JSON string
a = '{"name": "Bob", "languages": "English"}'
  
# deserializes into dict 
# and returns dict.
y = json.loads(a)
  
print("JSON string = ", y)
  
# JSON file
f = open ('employee.json', "r")
  
# Reading from file
data = json.loads(f.read())
  
# Iterating through the json
# list
for i in data['employee']:
    print(i)
  
# Closing file
f.close()