import json


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



settingsfile = open('./json_settings.json','r')
jsondata = settingsfile.read()
loadedjsonsettings = json.loads(jsondata)

print(loadedjsonsettings["Starthotkey"])