# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
N, M = input().split()
arr = np.zeros((int(N), int(M)))

while True:
	input_string = input()
	
	if input_string == "INPUT_END":
		break
	
	method, class_num, student_num, score = input_string.split()
	if method == "CLASS":
		arr[int(class_num)] += int(score)
	elif method == "GROUP":
		arr[:, int(student_num)] += int(score)
	elif method == "STUDENT":
		arr[int(class_num), int(student_num)] += int(score)

class_score_average = np.mean(arr[int(input())])
print(f"{class_score_average:.2f}")