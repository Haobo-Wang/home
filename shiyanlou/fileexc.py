#!/usr/bin/env python
# encoding: utf-8

# filename = input("Enter file path: ")
# try:
    # f = open(filename)
    # print(f.read())
    # f.close()
# except FileNotFoundError:
    # print("File not found.")
# f = open(filename)
# print(f.read())
# f.close()
filename = '/etc/protocols'
f = open(filename)
try:
    f.write('shiyanlou')
except:
    print('File write error')
finally:
    print("finally")
    f.close()
