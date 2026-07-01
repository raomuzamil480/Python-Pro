#Creat a Shoping Cart Programs

item = input('Please Enter  Item Name :')
price= float(input('Please Enter Prices Which items You Bought :'))
quantity=float(input('Please Enter Your Quantity :'))

totel= price * quantity

print(f"You Bought {item} with {quantity} quantity")

print(f'Your Totel bill is ${totel}')