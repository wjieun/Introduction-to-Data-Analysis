# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

numbers = list(map(int, input().split()))  # This will give you List of Integers
# Write your own code!
s = set(numbers)
num_of_unique_nums = len(s)
print(num_of_unique_nums)