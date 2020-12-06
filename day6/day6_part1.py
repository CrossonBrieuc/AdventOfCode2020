#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input_day6.txt","r") as input:
	wait=''
	for i in input:
		i=i[:-1]
		if i=='':
			val.append(wait)
			wait=''
		else:
			wait+=i
	val.append(wait)


# part 1

for x in val:
	lt=[]

	for y in x:
		if y not in lt:
			lt.append(y)

	res+=len(lt)

print("part1 :",res)

