#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input.txt","r") as inp:
	for i in inp:
		val.append((i[0], int(i[1:])))



# part 1

dirc = 'E'

dirc_list = ['E', 'S', 'W', 'N']

dirc_values = {
	'E':(0, 1),
	'W':(0, -1),
	'S':(1, -1),
	'N':(1, 1)
}

rotate_values = {
	'R':1,
	'L':-1
}

pos = [0, 0]  # [ +E -W  ,  +N -S ]


for inst, nbr in val:

	if inst in dirc_values:

		x = dirc_values[inst]	
		pos[x[0]] += nbr * x[1]

	elif inst in rotate_values:

		x = rotate_values[inst] * nbr // 90
		x += dirc_list.index(dirc)
		dirc = dirc_list[ x % 4 ]

	else:

		x = dirc_values[dirc]	
		pos[x[0]] += nbr * x[1]

	


res = sum([abs(i) for i in pos])

print("part1 :", res)
