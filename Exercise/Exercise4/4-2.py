students = [
  ['이이', 20211226, [61, 63, 59, 67, 55, 48, 61, 75, 45, 52]], 
  ['이황', 20200103, [77, 57, 81, 72, 51, 69, 75, 69, 61, 55]], 
  ['이도', 20180515, [62, 57, 87, 62, 77, 60, 91, 70, 67, 84]], 
  ['이산', 20190515, [98, 77, 89, 102, 76, 88, 86, 102, 74, 82]], 
  ['정약용', 20220805, [77, 98, 98, 109, 96, 94, 78, 113, 85, 78]]
]
dic = {}
for s in students:
	dic[s[0]] = [sum(s[2]) / len(s[2]), max(s[2]), min(s[2])]

name = input()
for i in dic[name]:
	print(i)
