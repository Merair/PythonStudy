#!/usr/bin/evn/python
# Author:Maira
""" 
#猜一次，判断大小
lucy_age = 18
guess_age = int(input("guess age:"))
if guess_age == lucy_age:
    print("you got it!")
elif guess_age > lucy_age:
    print("think smaller~")
else:
    print("think bigger~")
 """
count = 0
lucy_age = 18
while count<3:
    guess_age = int(input("guess age:"))
    if guess_age == lucy_age:
        print("yes,you got it.")
        break
    elif guess_age > lucy_age:
        print("think smaller...")
    else:
        print("think bigger!")
    count += 1
else:
    print("you have tried too many times...fuck off!")