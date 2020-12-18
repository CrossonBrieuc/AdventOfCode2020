#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input.txt","r") as inp:
	for i in inp:
		val.append(i[:-1].split(' = '))

# part 2

mask = ''
mem = {}

for x in val:
	if x[0] == 'mask':
		mask = x[1]
	else:
		nbr = x[0][4:-1]
		nbr = bin(int(nbr))[2:]
		nbr = '0'*(36 - len(nbr)) + nbr

		for i in range(36):
			if mask[i] != '0':
				nbr = nbr[:i] + mask[i] + nbr[i+1:]

		cbn = ['0']*nbr.count('X')

		for i in range(2**nbr.count('X')):
			new_nbr = ''
			i2=0
			for y in nbr:
				if y == 'X':
					new_nbr+=cbn[i2]
					i2+=1
				else:
					new_nbr+=y

			for y in range(len(cbn)):
				if cbn[y] == '0':
					cbn[y] = '1'
					break
				else:
					cbn[y] = '0'

			
			mem[new_nbr] = int(x[1])
			print(new_nbr, end='')
			print('\ractual nbr : ', end='', flush=True)


for x in mem:
	res+= mem[x]

	

print("\npart2 :", res)
