# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
year = int(input())
if (year%4==0 and year%100!=0) or year%400==0:
	print("True")
else:
	print("False")