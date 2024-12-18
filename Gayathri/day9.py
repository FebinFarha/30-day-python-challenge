*Problem 1: Symbol Calculator*


print("Symbol Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

match choice:
    case "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 + num2)
    case "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 - num2)
    case "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 * num2)
    case "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Result: ", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")
    case _:
        print("Invalid choice")



*Problem 2: Menu Price*



print("Menu")
print("1. Pizza - Rs. 80")
print("2. Burger - Rs. 100")
print("3. Chicken Lollipop - Rs. 150")
print("4. Cold Drink - Rs. 30")
print("5. Noodles - Rs. 50")

choice = int(input("Enter your choice (1-5): "))

match choice:
    case 1:
        print("Price of Pizza is Rs. 80")
    case 2:
        print("Price of Burger is Rs. 100")
    case 3:
        print("Price of Chicken Lollipop is Rs. 150")
    case 4:
        print("Price of Cold Drink is Rs. 30")
    case 5:
        print("Price of Noodles is Rs. 50")
    case _:
        print("Invalid choice")



*Problem 3: Number in Words*



num = int(input("Enter a number between 1 and 5: "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Invalid number")



*Problem 4: Weekdays*



day = input("Enter a day of the week: ")

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(day, "is a weekday")
    case "Saturday" | "Sunday":
        print(day, "is a weekend")
    case _:
        print("Invalid day")



*Problem 5: Size Chart*



measurement = int(input("Enter your measurement: "))

match measurement:
    case 29:
        print("Size: Small")
    case 42:
        print("Size: Medium")
    case 44:
        print("Size: Large")
    case 48:
        print("Size: Extra Large")
    case _:
        print("Unknown size")
