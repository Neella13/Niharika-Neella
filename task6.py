#1.print statement
print("*")
print("**")
print("***")
print("****")
print("*****")
#2.comments
num_1=5#assigning the value to variable
num_2=8#assigning the value to variable
""""here we are using the two variables and assigning the values to it 
both variables holding the integers and peforming the multiple operatior
and diplaying the result"""
result=(num_1*num_2)
print(result)#print is used to diplay the result
#3.data types
dict_1={'tittle':"the cat story's",'author':'vignanmartin','publish_year':1989}
print(dict_1)
#4.string operaions
age=input("enter a number: ")
float_con=float(age)
print(float_con)
#5.python keyword
#if keyword is used to create conditional statement
num_3=70
num_4=80
if num_3<num_4:print("num_3 is smaller than num_4 ")
#assert
message="hiiii"
#when condition is true ,then nothing happens
assert message=="hiiii"
#when condition is false,then assertion error is raised:
assert message=="hi"#error is arised
#6.swapping the values
num_5=15
num_6=10
num_5=num_5+num_6# num_5 becomes 25
num_6=num_5-num_6#num_6 becomes 15
num_5=num_5-num_6#num_5 becomes 10
#here without using the temporary variable we swap the values
print("after swapping:num_5=",num_5)
print("after swapping:num_6=",num_6)
#7.take input as 35 and convert it into integer
age=int(input("enter a age: "))
print(age+5)
#8.take the 2 inputs and perform the addition,subtraction,multiplication,division operations
num_7=int(input("enter a number: "))
num_8=int(input("enter a number: "))
print("addition:",num_7+num_8)
print("subtraction:",num_7-num_8)
print("multiplication:",num_7*num_8)
print("division:",num_7%num_8)

