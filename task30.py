#1.squaring all numbers
square_all=map(int,input("enter the numbers:").split())
'''here split method is used to split the string and then the string is converted into
the integer by using the int()'''
obj=map(lambda number:number**2,square_all)
print(list(obj))

#2.positive numbers using the filter function
filter_positive=map(int,input("enter a number:").split())
obj1=filter(lambda i:i>=0,filter_positive)
print(list(obj1))

#3.factorial of given number using reduce()
from functools import reduce 
factorial_number=int(input("enter a number:"))
obj=reduce(lambda x,y:x*y,range(1,factorial_number+1))
print(f"the factorial of {factorial_number}is {obj}")

#4.count the vowels in given string by using the reduce function
from functools import reduce 
count_vowels=input("enter the string:")
vowels='aeiouAEIOU'
obj=reduce(lambda acc,char:acc+(1 if char in vowels else 0),count_vowels,0)
print(obj)