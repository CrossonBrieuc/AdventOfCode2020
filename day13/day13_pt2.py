#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input.txt","r") as inp:
	for i in inp:
		val.append(i[:-1])


# part 2

depart = int(val[0])

ls = []

i=0
for x in val[1].split(','):
	if  x!='x':
		x=int(x)
		ls.append((x,i))
	i+=1

ls.sort(reverse=True)
print(ls)

nbr = - ls[0][1]
while True:
	nbr += ls[0][0] 
	test = True
	for x in ls[1:]:
		if (nbr+x[1]) % x[0] !=0:
			test=False
			break

	if test:
		res = nbr
		break

	print(nbr, end='')
	print('\ractual nbr : ', end='', flush=True)

print("\npart2 :", res)
