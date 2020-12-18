#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input.txt","r") as inp:
	for i in inp:
		val=(i[:-1].split(','))

# part 1
val = [int(i) for i in val]

lng = len(val)



done = False
for x in range(lng, 2020):
	if done == False:
		val.append(0)
		if val[-1] in val[:-1]:
			done = True
	else:
		val2 = val[:-1]
		val.append(val2[::-1].index(val[-1]) +1)
		done = False
		if val[-1] in val[:-1]:
			done = True

res = val[-1]

print("part1 :", res)
