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

done = False
for x in range(lng, 30000000):
	if done == False:
		val.insert(0 , 0) 
		if val[0] in val[1:]:
			done = True
	else:
		val.insert(0, val[1:].index(val[0]) + 1)
		done = False
		if val[0] in val[1:]:
			done = True

	print(x, end='')
	print('\ractual nbr : ', end='', flush=True)


res = val[0]
	
print("\npart2 :", res)
