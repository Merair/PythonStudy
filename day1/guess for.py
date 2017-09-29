#!/usr/bin/evn/python
# Author:Maira
Amy_age = 23
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == Amy_age:
        print("yes,you got it!")
        break
    elif guess_age < Amy_age:
        print("think bigger!")
    else:
        print("think smaller...")
else:
    print("you have tried too many times...fuck off")