# Make a Shoping Card Program use List ,sets , Touples

foods=[]
prices=[]
totle=0

while True:
    food=input('Please Enter Food You Want :')
    if food.lower()=='q':
        break
    else:
        price=float(input(f"Please Enter Price of {food} :"))
        foods.append(food)
        prices.append(price)

print('========Shoping Card ========')
for f in foods:
    print(f ,end=" ")
for p in prices:
    totle +=price
print()
print(f'Your Totle is :${totle}')

