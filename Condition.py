#   If Else
try:
    age = int(input('Please Enter your Age :'))

    if age >= 18:
     print('YOU ARE ADULT ')

    elif age >=0:
        print('YOU ARE NOT ADULT')
    else:
        print('PLEASE ENTER CORRECT AGE')
except ValueError:
    print("Please enter an integer (number only)")
