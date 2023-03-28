r = [("x",1),("x",2),("x",3),("y",1),("y",2),("z",1)]

d={}
for x,y in r:
    d.setdefault(x,[]).append(y)

print(d)    
