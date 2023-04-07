# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
height = float(input())
weight = float(input())
bmi = weight / (height * height)

if bmi >= 35:
	print("고도비만")
elif bmi >= 30:
	print("중도비만")
elif bmi >= 25:
	print("경도비만")
elif bmi >= 23:
	print("과체중")
elif bmi >= 18.5:
	print("정상")
else:
	print("저체중")