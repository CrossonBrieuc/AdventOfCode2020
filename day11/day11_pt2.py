#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

res=0
val=[]
lng=0

with open("input.txt","r") as inp:
	for i in inp:
		lng = len(i) - 1
		for x in i[:-1]:
			val.append(x)



# part 2

max_view = 20

dirc=[-lng-1, -lng, -lng+1, 1, lng+1, lng, lng-1, -1]

tt_lng = len(val)

def seat_test(i, pos, d):
	ni = pos + d
	if ni >= 0 and ni < tt_lng and abs(i%lng - ni%lng) <= max_view:
		if val[ni] == '#':
			return 1
		elif val[ni] == '.':
			return seat_test(i, ni, d)
		else:
			return 0
	else:
		return 0 

for z in range(1000):

	new_val = copy.copy(val)

	for i,x in enumerate(val):
		if x!='.':
			occupied = 0
			for d in dirc:
				occupied += seat_test(i, i ,d)

			if x == 'L' and occupied == 0:
				new_val[i] = '#'
			elif x == '#' and occupied >=5:
				new_val[i] = 'L'

	if new_val == val:
		break

	val = copy.copy(new_val)

	

res = val.count('#')

print("part2 :", res)
