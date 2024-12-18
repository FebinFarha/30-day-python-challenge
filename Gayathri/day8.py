_Problem 1: Calculate GCD/HCF of two numbers_


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD/HCF of the two numbers is:", num1)



_Problem 2: Calculate LCM of two numbers_


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = 0
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

lcm = (num1 * num2) // gcd
print("LCM of the two numbers is:", lcm)



_Problem 3: Compute prime factors of an integer_


num = int(input("Enter a number: "))

print("Prime factors of", num, "are:")
i = 2
while i * i <= num:
    if num % i:
        i += 1
    else:
        num //= i
        print(i)
if num > 1:
    print(num)



_Problem 4: Calculate grade based on marks_


marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

average_marks = sum(marks) / len(marks)

if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
elif average_marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Average marks:", average_marks)
print("Grade:", grade)



_Problem 5: Calculate sum of the given series_


n = int(input("Enter the value of n: "))

total_sum = 0
for i in range(1, n+1):
    sum = 0
    for j in range(1, i+1):
        sum += j
    total_sum += sum

print("Sum of the series:", total_sum)
