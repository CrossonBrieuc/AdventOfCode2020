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
			wait+=i+'|'
	val.append(wait)


# part 2

alf="abcdefghijklmnopqrstuvwxyz"

for x in val:
	lng=x.count('|')
	for y in alf:
		if x.count(y) == lng:
			res+=1

print("part2 :",res)

