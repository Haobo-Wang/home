#!/usr/bin/env python
# encoding: utf-8
str1 = "hello"
str2 = 'hello1'
str3 = 'hello,\'shiyanlou\''
str4 = "hello,'shiyanlou'"
str5 = 'hello,"shiyanlou"'
print(str1, str2, str3, str4, str5)
str6 = """hello,
nihaoa
shiyanlou
"""
print(str6)
print(str1 + str3)
print(str1, str1[0], str1[1], str1[-1], str1[:2], str1[3:])
print(str1[:0], str1[:1], str1[:2], str1[:3])
print(str1[0:], str1[1:], str1[2:], str1[3:])
print(len(str2))
