#list 
#indexing
my_list=[1,2,3,4,5,6,7]
num=my_list[0]
num1=my_list[4]
print(num,num1)
#slicing
num2=my_list[2:4]
print(num2)
#negative indexing 
num_3=my_list[-4]
print(num_3)
#skipping characters 
num_4=my_list[::5]
num_5=my_list[::-1]
print(num_4,num_5)
#list methods
list=[1,2,3,4,3,6,3,5,6,7,8,9]
list.append(0)
list.remove(4)
list.pop(4)
list.sort()
print(list)
list.reverse()
print(list)
num=list.count(3)
print(num)

