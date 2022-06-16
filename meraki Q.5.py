import json
def complex_num(a):
    if 'complex' in a:
        return complex(a['real'],a['img'])
    return a

b=json.loads('{"complex": true, "real": 4, "img": 5}', object_hook =complex_num)
k=json.loads('{"real": 4, "img": 3}', object_hook = complex_num)
print("Complex",b)
print("Without complex object",k)



