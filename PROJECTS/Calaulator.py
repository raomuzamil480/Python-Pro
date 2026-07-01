try:
    operator = input("Enter Operator (+, -, *, /): ")

    # check operator
    if operator not in ["+", "-", "*", "/"]:
        print("Please enter a valid operator only (+, -, *, /)")

    else:
        num1 = int(input("Enter Value One: "))
        num2 = int(input("Enter Value Two: "))

        if operator == "+":
            print(num1 + num2)

        elif operator == "-":
            print(num1 - num2)

        elif operator == "*":
            print(num1 * num2)

        elif operator == "/":
            print(num1 / num2)

except ValueError:
    print("Please enter integer values only")

except ZeroDivisionError:
    print("Cannot divide by zero")