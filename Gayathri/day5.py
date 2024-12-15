# Program to print the table of a number
number = int(input("Enter a number: "))
print(f"Table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Program to find the sum of the digits of a number
number = int(input("Enter a number: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
print(f"Sum of the digits: {sum_of_digits}")

# Program to find the product of the digits of a number
number = int(input("Enter a number: "))
product_of_digits = 1
while number > 0:
    digit = number % 10
    product_of_digits *= digit
    number //= 10
print(f"Product of the digits: {product_of_digits}")


sum_odd = 0
sum_even = 0
for i in range(12, 38):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}"
print("Numbers divisible by 11 but not by 2:")
for i in range(100, 501):
    if i % 11 == 0 and i % 2 != 0:
        print(i, end=" ")