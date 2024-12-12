print('python 30 day challenge')
print()
print('day 2')
print()
print('2.1 TRIGNOMETRIC FUNCTIONS CALCULATOR')
print()
import math
ang=int(input('Enter the angle:',))
x=math.sin(ang)
y=math.cos(ang)
z=math.tan(ang)
print('sin',ang,'=',x)
print('cos',ang,'=',y)
print('tan',ang,'=',z)
print()
print('2.2 AREA OF CYLINDER')
r=int(input('Enter the radius:',))
h=int(input('Enter the height:',))
ar=2*math.pi*r*(r+h)
print('Area of the cylinder:',ar)
print()
print('2.3 MEMBERSHIP OPERATOR')
str_='hello my name is febin'
print('my'in str_)
print('h' in str_)
print('to' not in str_)
print()
print('2.4 IDENTITY OPERATOR')
str1='hai'
str2='hey'
str3='hey'
print(str1 is not str2)
print(str2 is str3)
print()
print('2.5 QUOTIENT AND REMINDER')
num1=int(input('Enter the number:',))
num2=int(input('Enter the number:',))
quo=num1/num2
rem=num1%num2
print('quotient:',quo)
print('reminder:',rem)





