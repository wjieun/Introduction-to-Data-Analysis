# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

### online_shop 의 예시입니다. 학생 여러분들은 위와 비슷한 구조로 코드를 작성하셔도 좋고
### 학생 여러분들이 원하는 대로 코드를 작성하셔도 됩니다.
### 변수 online_shop_example은 채점에 사용되지 않습니다.
online_shop_example = [{"상품명" : "빼빼로", "상품 가격" : 1000, "상품 카테고리" : "과자", "제조사" : "농심"}, {"상품명" : "진라면 순한맛", "상품 가격" : 750, "상품 카테고리" : "라면", "제조사" : "오뚜기"}, {"상품명" : "진라면 매운맛", "상품 가격" : 700, "상품 카테고리" : "라면", "제조사" : "오뚜기"}, {"상품명" : "누드 빼빼로", "상품 가격" : 1500, "상품 카테고리" : "과자", "제조사" : "농심"}, {"상품명" : "스윙칩", "상품 가격" : 1700, "상품 카테고리" : "과자", "제조사" : "농심"}]
products = {}

while True:
	mode = int(input())
	
	if mode == 1:
		name = input()
		price = int(input())
		category = input()
		company = input()
		
		if name in products.keys():
			print('상품 존재')
		else:
			products[name] = [price, category, company]
			print('상품 등록')
		
	elif mode == 2:
		name = input()
		
		if name in products.keys():
			del products[name]
			print('상품 삭제')
		else:
			print('상품 없음')
		
	elif mode == 3:
		company = input()
		
		result = []
		for p in products:
			if products[p][2] == company:
				result.append(p)
		
		if len(result) == 0:
			print('제조사 없음')
		else:
			for r in sorted(result):
				print(r)
		
	elif mode == 4:
		sort_mode = int(input())
		
		s = []
		if sort_mode == 1:
			s = sorted(products.items(), key=lambda x:x[1][0])
		elif sort_mode == 2:
			s = sorted(products.items(), key=lambda x:x[1][0], reverse=True)
		
		idx = 0
		for i in s:
			print(i[0], i[1][0], i[1][1], i[1][2])
			idx += 1
			if idx == 4:
				break
		
	elif mode == 5:
		print(len(products), '상품 존재')
		break