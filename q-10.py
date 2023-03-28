N = [2,3,6,7,45,67,45,4,5,6,7,34,32,34,8,7]

unique= list()

for num in N:
    if num not in unique:
        unique= unique+[num]
        
print("unique num are : ")

for num in unique:
    print(num)
