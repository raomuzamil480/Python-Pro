# certain parament  used when argument is omitted
# postional-->simple
# default---->a=0
#keywoed----->Use in call funtion like ==>count(name='rao)

#Arbitary===========>*args,**kwargs

import  time

def count(start,end):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("DONE!")
count(1,2)

# All use to improve readablity of code

#  *args pass multiple non-key aruments
print("======================= *args===================")
def num(*args):
    totle=0
    for i in args:
        totle +=i
    return totle
print(num(1,2,3,4,5,6))

# key use in argument *kwargs
print("=====================*kwargs=================")

def Arg(**kwargs):
    for key in kwargs.items():
        print(key,end="")
Arg(city="lahor",adress="1234str")

#also use combine like (*args,**kwargs) in one  Function