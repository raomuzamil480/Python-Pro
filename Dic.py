# DIc is a key value pair value store {key:value}
# order and changeable but NO Duplicate
#
# dic={
#     "name":'Muzamil',
#     "age":21,
# }
# if dic.get('age'):
#     print('Yes Found ')
# else:
#     print("No Found")
# dic.update({"ego":23})
# dic.pop('age')
# dic.popitem()
# print(dic)
#
# key=dic.keys()
# print(key)

#===============================================

manue={
    "pizza":32,
    "patato":42,
    "likes":21,
}

totle=0
cart=[]
print("=====MANUE=====")
for key,value in manue.items():
    print(f"{key:10} {value:.2f}")
while True:
    food=input("Please Enter Food You Want (q to quite):")
    if food=='q':
        break
    elif manue.get(food) is not None:
        cart.append(food)
print('=============')

for i in cart:
    totle +=manue.get(i)
    print(i,end="")
print()
print(f"totle is :{totle:.2f}")