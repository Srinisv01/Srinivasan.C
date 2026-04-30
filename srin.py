'''
#1.
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
if a>=b and a>=c:
    print(a,"is the largest number")
elif b>=a and b>=c:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")

#2.
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
if a<=b and a<=c:
    print(a,"is the smallest number")
elif b<=a and b<=c:
    print(b,"is the smallest number")
else:
    print(c,"is the smallest number")

#3.
a = int(input("Enter the number: "))
if a>0:
    print("it is positive")
elif a==0:
    print("it is equal to zero")
else:
    print("it is negative")
#4.
a = int(input("Enter the no. of days: "))
if 1<=a and a<=5:
    print("your fine is", a*40, "paisa")
elif 6<=a and a<=10:
    print("your fine is", a*65, "paisa")
elif a>10:
    print("your fine is", a*80, "paisa")
else:
    print("invalid")
#6.
a = int(input("Enter the number: "))
if a%3==0:
    print(a, "is multiple of 3")
elif a%5==0:
    print(a, "is multiple of 5")
elif a%7==0:
    print(a, "is multiple of 7")
else:
    print(a, "is not the multiple of 3,5,7")
'''
#7.
t = str(input("enter the type of parcel: "))
n = int(input("Enter the amount of weight: "))
if t == "O":
    print("the type is ordinary")
elif t == "E":
    print("the type is express")
else:
    print("invalid type and weight")

if 1<=n and n>=100 and t == "O":
    print("the charge is $80")
elif 101<=n and n>=500 and t == "O":
    print("the charge is $150")
elif 501<=n and n>=1000 and t == "O":
    print("the charge is $210")
elif n>1000 and t == "O":
    print("the charge is $250")
if 1<=n and n>=100 and t == "E":
    print("the charge is $100")
elif 101<=n and n>=500 and t == "E":
    print("the charge is $200")
elif 501<=n and n>=1000 and t == "E":
    print("the charge is $250")
elif n>1000 and t == "E":
    print("the charge is $300")
























