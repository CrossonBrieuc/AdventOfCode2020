#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input.txt","r") as inp:
	for i in inp:
		val.append(i[:-1])



# part 1

val[0] = int(val[0])

restes = []

for x in val[1].split(','):
	if  x!='x':
		x=int(x)

		restes.append((x - val[0] % x, x))

restes.sort()

res = restes[0][1] * restes[0][0]

print("part1 :", res)
