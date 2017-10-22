#!/usr/bin/env python3
# encoding: utf-8

import sys

try:
    socialSecurity = 0
    income = int(sys.argv[1])
except ValueError:
    print("Input Error!")
if income <= 3500:
    print("穷的不需要纳税～")
else:
    taxableIncome = income - socialSecurity - 3500
    ratal = 0
    deduction = 0
    if taxableIncome <= 0:
        ratal = 0
        deduction = 0
    elif 0 < taxableIncome <= 1500:
        ratal = 0.03
        deduction = 0
    elif taxableIncome > 1500 and taxableIncome <= 4500:
        ratal = 0.10
        deduction = 105
    elif taxableIncome > 4500 and taxableIncome <= 9000:
        ratal = 0.20
        deduction = 555
    elif taxableIncome > 9000 and taxableIncome <= 35000:
        ratal = 0.25
        deduction = 1005
    elif taxableIncome > 35000 and taxableIncome <= 55000:
        ratal = 0.30
        deduction = 2755
    elif taxableIncome > 55000 and taxableIncome <= 80000:
        ratal = 0.35
        deduction = 5505
    else:
        ratal = 0.45
        deduction = 13505
    print("您的应纳税额是：", format(taxableIncome * ratal - deduction, ".2f"))
