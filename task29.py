#advance pythons
#lambda function
add=lambda a,b:a+b
print(add(1,32))
#filter function
def even(i):
    return i%2==0
obj=(even,[1,2,3,4,5,6,7,8])
print(list(obj))
#map function
obj=map(lambda i:i**2,[1,2,3,4,5,6,7,7,8])
print(list(obj))
#reduce function
from functools import reduce
list=[1,2,3,1,2,3]
def multiple(a,b):
    return a*b
obj=reduce(multiple,list)
print(obj)