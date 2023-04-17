# 학생 성적 평균을 반드시 아래 average 변수에 적용하세요.
average = 0.0
scores = []
while True:
	s = int(input())
	if s == -1:
		break
	scores.append(s)
average = sum(scores) / len(scores)
# 아래 코드에서 자동으로 학생 성적 평균이 반올림되어 출력됩니다.
print("{:.2f}".format(average))