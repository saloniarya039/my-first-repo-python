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



""" import addmultiplication
print(addmultiplication.x)
addmultiplication.sum(1,2)
addmultiplication.multiplication(2,3)
 """







""" irrigation_method = int(input())
area_acres = int(input())
a = float(area_acres*40)
b = float(area_acres*85)
if irrigation_method == 0:
    print(a)
else:
    print(b) """


""" seat_category = input()
showtime = input()
num_ticket = int(input())

a = (num_ticket*350)
b = (num_ticket*250)
c = (num_ticket*200)
d = (num_ticket*150)

if seat_category == "premium" and showtime == "weekend":
    print(f"{a:.2f}")
elif seat_category == "premium" and showtime == "weekday":
    print(f"{b:.2f}")
elif seat_category == "standard" and showtime == "weekend":
    print(f"{c:.2f}")
else:
    print(f"{d:.2f}") """


""" units_consumed = float(input())
is_peak_hour = input()
a = (units_consumed*9)
b = (units_consumed*5)
if is_peak_hour == 1:
    print(f"{a:.2f}")
else:
    print(f"{b:.2f}") """





