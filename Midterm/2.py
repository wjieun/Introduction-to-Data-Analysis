
tools = {1: '전동드라이버', 2: '드릴', 3: '몽키스패너', 4: '드라이버', 5: '망치', 6: '실리콘', 7: '손전등', 8: '전류계', 9: '풀', 10: '백시멘트'}
price = {1: 1000000, 2: 3000000, 3: 500000, 4: 200000, 5: 400000, 6: 300000, 7: 250000, 8: 700000, 9: 450000, 10: 650000}

print("시공할 공사를 입력하세요")
l = []
total = 0
while True:
	num = int(input())
	if num == 0:
		break
	if tools[num] not in l:
		l.append(tools[num])
	total += price[num]
print("챙겨야 하는 준비물: ", l)
print("시공비 총액: ", total, "원")