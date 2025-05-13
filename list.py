# --- List in python ---

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
