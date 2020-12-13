#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input.txt","r") as inp:
	for i in inp:
		val.append((i[0], int(i[1:])))


# part 2

dirc = 0
dirc_list = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

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

pos_wp = [10, 1]  # [ +E -W  ,  +N -S ]

pos = [0, 0]

for inst, nbr in val:

	if inst in dirc_values:

		x = dirc_values[inst]	
		pos_wp[x[0]] += nbr * x[1]

	elif inst in rotate_values:

		x = rotate_values[inst] * nbr // 90
		
		if pos_wp[0] <= 0 and  pos_wp[1] <= 0:
			dirc = (2 + x) % 4
		elif pos_wp[0] < 0:
			dirc = (3 + x) % 4
		elif pos_wp[1] < 0:
			dirc = (1 + x) % 4
		else:
			dirc = (0 + x) % 4

		if x % 2 == 1:
			pos_wp = [pos_wp[1], pos_wp[0]]

		pos_wp[0] = abs(pos_wp[0]) * dirc_list[dirc][0]
		pos_wp[1] = abs(pos_wp[1]) * dirc_list[dirc][1]

	else:

		pos[0] += pos_wp[0] * nbr
		pos[1] += pos_wp[1] * nbr



res = sum([abs(i) for i in pos])

print("part2 :", res)
