#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]
with open("/home/bcr/PycharmProjects/AdventOfCode/input_day2.txt","r") as input:
	input.readline()
	for i in input:
		val.append(i)

# part 1
for x in val:
	x=x.split(' ')

	interval=[int(i) for i in x[0].split('-')]

	lettre=x[1][0]

	cpt=x[2].count(lettre)

	if cpt>=interval[0] and cpt<=interval[1]:
		res+=1

print("part1 :",res)

# part 2
res=0
for x in val:
	x=x.split(' ')

	pos=[int(i)-1 for i in x[0].split('-')]

	lettre=x[1][0]

	try:
		if x[2][pos[1]]==lettre!=x[2][pos[0]]:
			res+=1
		elif x[2][pos[0]]==lettre!=x[2][pos[1]]:
			res+=1
	except:
		continue

print("part2 :",res)
