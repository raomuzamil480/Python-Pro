# Use Nested Loop

num=((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))

for i in num:
    for a in i:
        print(a,end=" ")
    print()
