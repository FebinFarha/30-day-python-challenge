print('python 30 day challenge')
print()
print('day 3')
print()
print('3.1 DOLLARS TO RUPEES CONVERTER')
print()
doll=float(input('Enter the amount in dollars:'))
rup=doll*84.8
print('USD =',doll,'INR =',rup)
print()
print('3.2 SWAPPING OF TWO VARIABLES')
print()
n1=int(input('Enter the number:'))
n2=int(input('Enter the number:'))
print('Before swapping a=',n1,'b=',n2)
n1,n2=n2,n1
print('After swapping a=',n1,'b=',n2)
print()
print('3.3 TO CHECK WHETHER THE GIVEN NUMBER IS > 50')
print()
num=int(input('Enter the number:',))
if num > 50:
    print(num,' is > 50 HURRAY')
print()
print('3.4 TO CHECK WHETHER THE GIVEN NUMBER IS POSITIVE')
print()
num=int(input('Enter the number:',))
if num > 0:
    print(num,'is a positive number')
print()
print('3.5 TO CHECK WHETHER THE GIVEN NUMBER IS  EVEN OR ODD')
num=int(input('Enter the number:',))
if num % 2==0:
    print(num,'is even')
else:
    print(num,'is odd')
print()
print('3.6 TO CHECK WHETHER THE GIVEN NUMBER IS DIVISIBLE BY 2')
num=int(input('Enter the number:',))
if num % 2==0:
    print(num,'is divisisble by 2')
else:
    print(num,'is not divisible by 2')
print()
print('3.7 TO CONVERT KILOMETER TO MILES AND VICE VERSA')
print()
dis=float(input('Enter the distance:'))
unt=input('Enter the unit(km or mi)')
if unt==km:
    mils=dis*0.62137
    print('MILES 'mils)
elif unt==mi:
    kilmtr=dis/0.62137
    print('KILOMETER 'kilmtr)
else:
    print('Invalid unit')
print()
print('3.8 TO CHECK WHETHER THE GIVEN NUMBER IS +VE,-VE OR 0')
num=int(input('Enter the number:',))
if num > 0:
    print(num,'is positive')
if num < 0:
    print(num,'is negative')
else:
    print(num,'is 0')