# --- List in python ---
'''
l1 =[]
for i in range(5):
    num = int(input("Enter next no :"))
    l1.append(num)

print(l1)
print("Print using for loop")
for idx in range(len(l1)):
    print(l1[idx])

print("print using Another for loo")
for e in l1: 
#e will have one element at a time
    print(e)
'''

# given list l1 add 10 to every element
# store in new list
# display both  lists
'''
l1=[100,5,7,10,50]
new_list=[]
for e in l1:
    t = e+10
    new_list.append(t)
print(l1)
print(new_list)
new_list=[]
for idx in range(len(l1)):
    t = l1[idx]+10
    new_list.append(t)
print(l1)
print(new_list)

l1=[100,5,7,10,50]
l2=[e for e in l1]
print(l2)'''

'''
l1 = [10,20,34,23,67,89]
num = int(input("Enter a number to be searched in 11 :"))
if num in l1:
    print(num, "is present in l1")
else:
    print(num, "is NOT present in l1")


l1=[10,20,34,10,23,67,89,23,34,99]
# remove duplicate elements and put in new list
# new list should not have duplicate elements
l2=[]
for e in l1:
  if e not in l2:
     l2.append(e)
print("Unique values in l1 are ")
print(l2)
'''
# Take a list l1 and print sum of 
# all numbers in the list

l1 = [10,34,23,56,78]
print("Addition of all elements is ")
total=0
for idx in range(len(l1)):
    total = total + l1[idx]
print(total)

print("Multiplication of all elements is ")
mult=1
for idx in range(len(l1)):
    mult =  mult * l1[idx]
print(mult)

print("Minimum number in the list is .. ")
l1=[10,5,2,7,9,55,1,43]
min_num = l1[0]
for e in l1:
    if e < min_num:
        print(min_num)

print("Maximum number in the list is ...")
l1=[10,5,2,7,9,55,1,43]
max_num = l1[0]
for e in l1:
    if e > max_num:
        max_num = e
print(max_num)
