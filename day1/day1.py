#!/usr/bin/env python
# -*- coding: utf-8 -*-

res='NA'
val=[]
with open("input_day1.txt","r") as input:
	for i in input:
		val.append(int(i))

# part 1
for x in val[:len(val)//2+1]:
	for y in val:
		if x!=y and x+y==2020:
			res=[x,y,x*y]

print(res)

# part 2
for x in val[:len(val)//2+1]:
	for y in val:
		for z in val:
			if x!=y!=z and x+y+z==2020:
				res=[x,y,z,x*y*z]

print(res)