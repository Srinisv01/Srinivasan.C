'''
#1.
a=int(input("Enter the number(a): "))
b=int(input("Enter the number(b): "))
if a>b:
    print ("b is smallest number")
else:
    print ("a is smallest number")

#2.
a=int(input("Enter the number(a): "))
b=int(input("Enter the number(b): "))
if a<b:
    print (b, "is the largest number")
else :
    print (a, "is the largest number")
  
#3.
number=int(input("Enter the number: "))
if number>=0:
    print(number)
else:
    print(-(number))
#4.
number=int(input("Enter the number: "))
if number%2==0:
  print ("it is even")
else:
    print("it is odd")

#5.
number=int(input("Enter the number: "))
if number%5==0:
    print("it is the multiple of 5")
else:
    print("it is not the multiple of 5")

#6.
number=int(input("Enter the number: "))
if number%10==0:
    print("it is the multiple of 10")
else:
    print("it is not the multiple of 10")

#7.
number=int(input("Enter the number: "))
if number>=10 and number<100:
    print("it is a two digit number")
else :
    print("it is not a two digit number")

#8.
number=int(input("Enter the number: "))
if number>=100 and number<1000:
    print("it is a three digit number")
else:
    print("it is not a three digit number")

#9.
a=int(input("Enter the number: "))
if a%10==0:
    print("it ends with zero")
else:
    print("it does not ends with zero")

#10.
a=int(input("Enter the number: "))
if a**2>=50:
    print("the square of",a, "is above 50")
else:
    print("the square of",a, "is below 50")

#11.
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
sub=a-b
print("sub: ", sub)
if sub==0:
    print("subtract of",a, "and",b, "is zero")
else:
    print("subtract of",a, "and",b, "is not zero")

#12.
mark=int(input("Enter the mark: "))
if mark>=50:
    print("you are pass")
else:
    print("you are fail")

#13.
number=int(input("Enter the number: "))
if number%10==0:
    print("it is divisible by 10")
else:
    print("it is not divisible by 10")

#14.
a=int(input("Enter the number(a): "))
b=int(input("Enter the number(b): "))
if a<b:
    print (b, "is the biggest digit")
else :
    print (a, "is the biggest digit")

#15.
a=int(input("Enter the choice: "))
if a==1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")

#16.
a=int(input("Enter the choice: "))
if a==1:
    print("You can go out and play")
else:
    print("You cannot go out and play")

#17.
length=int(input("Enter the length: "))
breadth=int(input("Enter the breadth: "))
if length==breadth:
    print("they are same")
    print("so, it is a square")
else:
    print("they are not same")
    print("so, it is a rectangle")

#21.
n = int(input("Enter the number: "))
if n%15==0:
    print(n, "is a multiple of both 5 and 3")
else:
    print(n, "is not a multiple of both 5 and 3")
#22.
n = int(input("Enter the number: "))
if n>=100 and n<1000:
    print(n, "is a three digit number")
    if n%10==0:
        print(n, "is a multiple of 10")
    else:
        print(n, "is not a multiple of 10")
else:
    print(n, "is not a three digit number")
#23.
n = int(input("Enter the number: "))
if n>=100 and n<1000:
    print(n, "is a three digit number")
    if n%10==0 and n%2==0 and n%5==0:
        print(n, "is a multiple of 2, 5 and 10")
    else:
        print(n, "is not a multiple of 2, 5 and 10")
else:
    print(n, "is not a three digit number")
#24.
n = int(input("Enter the number: "))
a = int(input("Enter the number: "))
if a%2==0 and n%2==0:
    print(n*a)
else:
    print(n+a)
#25.
n = int(input("Enter the number: "))
if n%10==7 or n%7==0:
    print(n, "is a buzz number")
else:
    print(n, "is not a buzz number")
'''


        












