Day 2
Program 1
import math
n=int(input("Enter the number"))
s=math.sin(n)
c=math.cos(n)
t=math.tan(n)
print("Trignometric functions")
print("sin",n,"=",s)
print("cos",n,"=",c)
print("tan",n,"=",t)

Program 2
import math
h=int(input("Enter the height"))
r=int(input("Enter the radius"))
a=math.pi*2*r*(r+h)
print("Area of the cylinder=",a)

Program 3
text="hi how are you?"
print("how" in text)

Program 4
str1=("hi")
str2=("hello")
str3=("hi")
print(str1 is str2)
print(str2 is str3)
print(str3 is str1)

Program 5
a1=int(input("Enter the number"))
a2=int(input("Enter the number"))
a=a1//a2
aa=a1%a2
print("Quotient of ",a1,"and",a2,"is",a)
print("Reminder of ",a1,"and",a2,"is",aa)