#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input.txt","r") as inp:
	for i in inp:
		val=(i[:-1].split(','))

# part 2

val = [int(i) for i in val[::-1]]

print(val)

lng = len(val)

for x in range(lng, 30000000):
	try:
		nb = val[1:].index(val[0]) + 1
	except:
		nb = 0
	val.insert(0, nb)
		
	print(x, end='')
	print('\ractual nbr : ', end='', flush=True)


res = val[0]
	
print("\npart2 :", res)
