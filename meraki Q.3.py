import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
b=open("dict.json","w")
c=json.dump(a,b,indent=4)




