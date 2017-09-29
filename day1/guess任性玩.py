#!/usr/bin/evn/python
# Author:Maira
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
    if count == 3:
        continue_confirm = input("Do you want to keep guessing..?")
        if continue_confirm != "n":
            count = 0
