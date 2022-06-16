import json
a={'4': 5, '6': 7, '1': 3, '2': 4}
b=json.dumps(a,sort_keys=True, indent=4)
print(b)




