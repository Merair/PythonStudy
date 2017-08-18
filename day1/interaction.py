#!/usr/bin/evn/python
#-*- coding:utf-8 -*-
username = input("username:")
password = input("password:")
name = input("name:")
age = input("age:")
salary = input("salary:")
print(username,password)

info = '''
---------------  info of %s  ----------------
name:%s
age:%s
salary:%s
'''% (name,name,age,salary)
print(info)