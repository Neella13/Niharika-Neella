#python functions
#add functions
def add(a,b):
    return a+b
obj=add(6,7)
print(obj)
#2.square functions
def square(x):
    return x**2
obj=square(6)
print(obj)
#3.factorial functions
def factorial(n):
    result=1
    for i in range(1,n+1):
      result*=i
    return(result)
n=int(input("enter a number:"))
if n>0:
    print(f"the factorial{n} is {factorial(n)}")
else:
    print("factorial is not defined for negtive numbers")
#4.maximum function
def maximum(list):
    maximum_value=max(list)
    print(f"the maximum value is{maximum_value}")
    return
list=[10,4,7,30,7,4,9,2]
maximum(list)

      

