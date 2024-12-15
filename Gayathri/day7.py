from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

# Display the result
print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))


    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


n = int(input("Enter a number: "))

# Calculate cubes
print("Cubes of numbers from 1 to", n)
for i in range(1, n + 1):
    print(f"Cube of {i}: {i**3}) 


    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


n_terms = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci(n_terms))



for i in range(1, 6):
    print(str(i) * 4)

# Python script that displays various date #and time formats:


from datetime import datetime

# Get current date and time
now = datetime.now()

# Display various date and time formats
print("Current date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current year: ", now.strftime("%Y"))
print("Month of year: ", now.strftime("%B"))
print("Week number of the year: ", now.strftime("%W"))
print("Weekday of the week: ", now.strftime("%A"))
print("Day of year: ", now.strftime("%j"))
print("Day of the month: ", now.strftime("%d"))
print("Day of week: ", now.strftime("%w"))
