#coding exercise :
#1.create a tuple and print it
tuple=('niharika',20,'black')
print(tuple)

#2.access tuple elements
tuple1=('sunday','monday','tuesday','wednesday','thrusday','friday','saturday')
result=tuple1.index('tuesday')
print(result)

#3.tuple concatenation
odd_tuple=(1,3,5)
even_tuple=(2,4,6)
tuple=odd_tuple+even_tuple
print(tuple)

#4.tuple unpacking
tuple=(6,7)
length,width=tuple
print("length:",length)
print("width:",width)
print(f"area={length*width}")

#5.check if an element exists
tuple=(1,2,5,(6,7,8),'niha',8.9)
result='niha' in tuple
print(result)

#6.program to generate a bill for supermarket purchase
items=[("apple",99),("banana",99),("milk",49)]
total=0.0
print("item\t""price")
print("-"*14)  
for(i,j) in items:
    print(f"{i}\t{j}")
    total+=j
print("-"*14)
print("Total\t",total)

#sets exercise
#1.set intersection
set1={1,2,3,4,5}
set2={4,6,7,8}
set=set1.intersection(set2)
print(set)

#2.set union
set1={1,2,3,4,5}
set2={4,5,6,}
set=set1.union(set2)
print(set)

#3.set difference
set1={1,2,3,4,5}
set2={4,5,6,}
set=set1.difference(set2)
print(set)

#4.set symmetric difference
set1={1,2,3,4,5}
set2={4,5,6,}
set=set1.symmetric_difference(set2)
print(set)

#5.set membership test
set={2,3,4,5,6}
result=3 in set
print(result)
          
