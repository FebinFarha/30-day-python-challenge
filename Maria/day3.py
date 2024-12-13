Day 3
Program 1
dollars=int(input("Enter the amount in Dollars($)"))
rupees=dollars*79.40
print("Rupees =",rupees,"Rs/-")

Program 2
a=int(input("Enter the number"))
b=int(input("Enter the second number"))
print(a,",",b)
print("After Swap",b,",",a)

Program 3
number=int(input("Enter the number"))
if (number>50):
    print("HURRAY!!!")
else:
    print("Still Chasing...")

Program 4
number=int(input("Enter the number"))
if(number>0):
    print("Positive Number!!!")

Program 5
number=int(input("Enter the number"))
if(number>0):
    print("Positive Number!!!")

Program 6
number=int(input("Enter the number"))
if (number%2==0):
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2")

Program 7
n=int(input("Enter the value:"))
dist=input("Enter k for converting kilometer to miles and m for converting miles to kilometer:")
km=n*0.62137
mi=n*1.609344
match(dist):
    case'k':
        print(n,"kilometers =",km,"miles")
    case'm':
        (n,"miles =",mi,"kilometers")

Program 8
number=int(input("Enter the number"))
if(number>0):
    print("Positive Number")
elif(number==0):
    print("Number is Zero:)")
else:
    print("Negative Number")