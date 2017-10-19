#!/usr/bin/env python
# encoding: utf-8

strlist = ['hello', 'shiyanlou', '.com']
for item in strlist:
    print(item)

for abc in range(0, 10):
    print(abc)
w = 100
while w > 10:
    print(w)
    w-=10
for aa in range(10):
    if aa == 5:
        break
    print(aa)
for bb in range(10):
    if bb == 5:
        continue
    print(bb)
