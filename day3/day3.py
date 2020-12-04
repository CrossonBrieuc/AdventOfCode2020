#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[".#.......#...........#........."]
with open("/home/bcr/PycharmProjects/AdventOfCode/input_day3.txt","r") as inp:
	inp.readline()
	for i in inp:
		val.append(i)



# part 1
lng=len(val[0])
pos=0
for x in val:
	if x[pos%lng]=="#":
		res+=1
	pos+=3

print("part1 :",res)


# part 2
ls_res=[0]*5
deplacement=[[1,1],[3,1],[5,1],[7,1],[1,2]]
for i,d in enumerate(deplacement):
	print(i,d)
	pos=0
	for i2,x in enumerate(val):
		if i2%d[1]==0:
			if x[pos%lng]=="#":
				ls_res[i]+=1
				print(ls_res)
			pos+=d[0]

res=1
for x in ls_res:
	res*=x

print("part2 :",res)