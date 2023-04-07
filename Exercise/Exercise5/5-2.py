# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np

# 점수를 담아둘 어레이를 생성하세요
arr = np.zeros(100)
N = int(input())

# 입력되는 점수 변동 반영을 INPUT_END 입력까지 반복하세요
while True:
	input_string = input()
	if input_string == "INPUT_END":
		break
	
	a, b = input_string.split()
	if int(a) >= 0 and int(a) < N:
		arr[int(a)] += int(b)

# 특정 학생의 점수를 정수로 출력하세요!
score_answer = arr[int(input())]
print(int(score_answer))