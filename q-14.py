from heapq import nlargest
a = {'p':100,'q':200,'r':300,'s':400,'t':500}

three_largest = nlargest(3,a,key=a.get)

print(three_largest)
