def uniquelist(data1):
    x = []
    for p in data1:
        if p not in x:
            x.append(p)
    return x
datalist=[]

n = int(input("enter total element in a list : "))

for k in range(n):
    data=int(input("enter in data list : "))
    datalist.append(data)

print("original list",datalist)
print("unique list",uniquelist(datalist))
