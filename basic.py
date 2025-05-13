# This is a comment in python  ----
#print("Hello world")

"""
This is a doc string
It can be used as multi-line comment
It can be  single/dobule quotes
"""
# --- Basic User Input ---

print("--------------- Let's print your name ------------------")

name = input("Your name please: ")

print("Hi,",name,"lets use some basic stuff of python")

# --- Conditional statements --- 
# if else & elif satement

print("--------- The Even odd number game using if else -----------")

num = int(input("Enter a number bewtween to get if it is even or odd :"))

if num % 2 == 0:
   print("even")
elif num % 2 == 1:
   print("odd")
else:
   print("Wrong input")

# --- Looping statements ---
# For loop basic

print("----------- Now, the looping game --------------")

num1 = int(input("Enter a number :"))

for i in range(num1):
    num = int(input("Enter next number :"))
    print(num)


# While loop basic

print("----------- Now,some more looping --------------")

num2 = int(input("Enter a number :"))
n=2
while n < num:
    if num%n == 0:
        print("Not a prime")
        break 
    n=n+1
else: 
   print("Prime")





