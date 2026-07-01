# username not greater then 12
# username not space between
# usernname not contain digit

username= input('Plesae Enter Name :')

if len(username) > 12:
    print('user not define because name much length')
elif not username.find(" ")==-1:
    print(f'space not use {username}')
elif not username.isalpha():
    print('number not use')
else:
    print(f'Welcome My Dear {username}')
