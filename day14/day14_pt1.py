#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input.txt","r") as inp:
	for i in inp:
		val.append(i[:-1].split(' = '))

# part 1

mask = ''
mem = {}

for x in val:
	if x[0] == 'mask':
		mask = x[1]
	else:
		nbr = bin(int(x[1]))[2:]
		nbr = '0'*(36 - len(nbr)) + nbr

		for i in range(36):
			if mask[i] != 'X':
				nbr = nbr[:i] + mask[i] + nbr[i+1:]

		mem[x[0]] = int(nbr, 2)


for x in mem:
	res+= mem[x]

print("part1 :", res)
