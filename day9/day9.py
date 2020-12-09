#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input_day9.txt","r") as inp:
	for i in inp:
		val.append(int(i[:-1]))



# part 1

lng = 25
index_max = 0

def sum_test(index, nbr):

	ls = val[index-lng:index]
	result = False

	for x in ls:
		for y in ls:
			if y!=x and x+y==nbr:
				result = True
				break

	return result


for i,nbr in enumerate(val[lng:]):

	i+=lng
	test = sum_test(i, nbr)

	if test == False:
		res = nbr
		index_max = i
		break


print("part1 :",res)




# part 2

res_2 = -1

for sum_lng in range(1000):

	for i in range(len(val[:index_max])-sum_lng-1):

		ls=val[i:i+sum_lng]

		if sum(ls) == res:
			res_2 = min(ls) + max(ls)
			break

	if res_2 >= 0:
		break


print("part2 :",res_2)
