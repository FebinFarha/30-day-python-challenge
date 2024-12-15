# Program to print the Fibonacci series
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
# Program to count the number of vowels in a string
string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
# Program to find the sum of squares of n natural numbers
n = int(input("Enter the value of n: "))
sum_of_squares = sum(i**2 for i in range(1, n + 1))
print(f"Sum of squares of {n} natural numbers: {sum_of_squares}")
# Program to find the sum of cubes of n natural numbers
n = int(input("Enter the value of n: "))
sum_of_cubes = sum(i**3 for i in range(1, n + 1))
print(f"Sum of cubes of {n} natural numbers: {sum_of_cubes}")
# Program to check if a number is an Armstrong number
number = int(input("Enter a number: "))
temp = number
sum_of_powers = 0
num_digits = len(str(number))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")