#1.vowels or not
vowels=['a','e','i','o','u']
letter=input("enter the letter: ")
if letter==vowels:
    print(f"{letter} is vowel")
else:
    print(f"{letter} is consonant")    
    
#2.age group caluculation
#using elif
age=int(input("enter the age: "))
if age<=12:
    print(f"the mentioned age {age} comes under child category")
elif age<=17:
     print(f"the mentioned age {age} comes under teenager category")
elif age<=64:
     print(f"the mentioned age {age} comes under adult category")
else:
     print(f"the mentioned age {age} comes under senior category")  

#3.number classifier
# if-elif-else
num=int(input("enter the number: "))
if num==0:
     print(f"the number {num} is zero")
elif num>0:
     print(f"the number {num} is positive") 
else:
     print(f"the number {num} is negative")
                           
#4.leap year 
year=int(input("enter the year: "))
if year%4==0 and year%100!=0 or year%400==0:
     print(f"the year {year} is leap year")
else:
     print(f"the year {year} is not a leap year")  

#5.calculator 
num_1=int(input("enter the number: "))
num_2=int(input("enter the number: "))
operator=input("enter the operator: ")
if operator=="+":
    print(num_1+num_2)
elif operator=="-":
     print(num_1-num_2)
elif operator=="*": 
     print(num_1*num_2) 
elif operator=="/":    
     print(num_1/num_2)
else:
     print("the operator is invalid")

#6.short hand if
x=8
print("even" if x%2==0 else "odd")  

#7.discount calculator
orginal_cost=float(input("enter the cost: "))
discount=float(input("enter a discount: "))
final_cost=orginal_cost-(orginal_cost*(discount/100))
print(final_cost)

#8.body mass index program
weight=float(input("enter the weight: "))
height=float(input("enter a height: "))
BMI=float(weight/(height**2))
print(BMI)