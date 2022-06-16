import json
a={"shopping_list":
        {"chaco":"15",
        "Biscuits":"50",
        "Diary_milk":"30",
        "ice_cream":"20",
        } 
}

n=input("enter a item")
n1=int(input("enter the quantity"))
for i in a:
        for j in a[i]:
                if n in a[i]:
                        if j==n and int(a[i][j])>=n1:
                                b=int(a[i][j])-n1
                                a[i][j]=str(b)
                                break
                elif j!=n:
                        print("not available")
                        break
n2=open("data2.json","w")
json.dump(a,n2,indent=4)


