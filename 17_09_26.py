""" for x in range(5,0,-1):
    for y in range(x):
        if y % 2 == 0:
            print("#", end=" ")
    else:
        print("*")
        print(y,end=" ")
print() """

""" group = [1,2,3,4,5]
search = int(input("Enter the element in search:"))
for elements in group:
    if search == elements:
        print("elements found in group")
    else:
        print("not found")
        break """


""" cart = [10,20,500,700,50,60]
for item in cart:
    if item>= 500:
        continue
    print("item:",item) """



""" cart = [10,20,500,700,50,60]
for item in cart:
    if item>= 500:
        break
    print("item:",item) """




""" i = 1
while i<= 1:
    if i == 500:
        i += 1
        break
    print(i)
    i += 1 """



""" for x in range(1, 500):
    for y in range(x):
        if y % 5 & 3 == 0:
            print("Hi", end=" ")
 """


""" num =1
while num<10:
    print("Hi")
    num+=1
else:
    print("Hello") """


""" for x in  range(1,5):
    print("HI")
else:
    print("Hello") """



""" group = [1,2,3,4,5]
search = int(input("Enter the elemetns in search:"))
for elements in group:
    if search == elements:
        print("elements found in group")
        break
    else: 
        print("element not found")
 """

""" 
total = 0
while True:
    num = int(input("Enter a number(or 0 to exit):"))
    total+= num 
    print(num) """



import addmultiplication
print(addmultiplication.x)
addmultiplication.sum(1,2)
addmultiplication.multiplication(2,3)
