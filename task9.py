#1.area of rectangle
length=int(input("enter the length: "))
width=int(input("enter the width: "))
area=length*width
print(area)
#3.program to convert celsius to fahrenheit
celsius=float(input("enter the celsius"))
Fahrenheit=(celsius * 9/5)+32
print(Fahrenheit)
#2.increment an decrement
num_1=7
num_1 +=5#+ operator is used to increment the value in variable
num_2=8
num_2 -=4 # - operator is used to decrement the value in variable
#4.simple intrest
principal_amount=float(input("enter the principal amount: "))
rate=float(input("enter the rate of intrest: "))
time=float(input("enter the time in years: "))
intrest=(principal_amount*rate*time)/100
print(f"the simple intrest is {intrest}")
#5.concatenate
num_3=input("enter a number: ")
num_4=input("enter a number: ")
result=num_3+num_4
print(result)
#6.kilometers  to miles
kilometer=float(input("enter the distance: "))
conv_fac=0.621371
miles=kilometer*conv_fac
print(miles)