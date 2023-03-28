import operator

r = {1:2,3:4,5:6,2:1,0:0}
print("original dictionary:",r)

sorted_r = sorted(r.items(),key=operator.itemgetter(1))

print("dictionary in ascending order by value:",sorted_r)

sorted_r = dict(sorted(r.items(),key=operator.itemgetter(1),reverse=True))
print("dictionary in descending order by value:",sorted_r)
