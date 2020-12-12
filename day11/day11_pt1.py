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



# part 1

dirc=[-lng-1, -lng, -lng+1, 1, lng+1, lng, lng-1, -1]

tt_lng = len(val)

for z in range(1000):

	new_val = copy.copy(val)

	for i,x in enumerate(val):
		if x!='.':
			occupied = 0
			for d in dirc:
				ni = i + d
				if ni >= 0 and ni < tt_lng and abs(i%lng - ni%lng) <= 1:
					if val[ni] == '#':
						occupied +=1

			if x == 'L' and occupied == 0:
				new_val[i] = '#'
			elif x == '#' and occupied >=4:
				new_val[i] = 'L'

	if new_val == val:
		break

	val = copy.copy(new_val)


res = val.count('#')

print("part1 :", res)


# part 2


#print("part2 :",res_2)
