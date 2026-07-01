import  time

myTime=int(input('Please Enter Time :'))
for i in range(myTime,0,-1):
    secound=i%60
    mints=int(i/60)%60

    time.sleep(1)

    print(f"{mints:02}:{secound:02}")
