try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Invalid input.")
