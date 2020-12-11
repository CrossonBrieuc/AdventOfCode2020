#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input_day10.txt","r") as inp:
	for i in inp:
		val.append(int(i[:-1]))



# part 1

val.sort()

last_val=0
one_jolt=0
tree_jolt=0

for x in val:
	if x - last_val == 1:
		one_jolt+=1
	else:
		tree_jolt+=1
	last_val = x


res = one_jolt * (tree_jolt + 1)

print("part1 :",res)


# part 2

test = False
last_val=0
den=[]

for x in val:
	if x - last_val == 1:
		if test == False:
			den.append(1)
		else:
			den[len(den)-1]+=1
		test = True
	else:
		test = False
	last_val = x

res_2 = 1

for x in den:
	if x == 3:
		res_2*=4
	elif x == 4:
		res_2*=7
	else:
		res_2*=x

print("part2 :",res_2)
