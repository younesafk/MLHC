import random


x=random.randint(0,50)
count=1

y=int(input("enter a number"))

while(y!=x):
    if(y>x):
        print("lower")
        y=int(input("enter a number"))
        count+=1
    elif(y<x):
        print("higher")
        y=int(input("enter a number"))
        count+=1
    

print(count,"tries")

