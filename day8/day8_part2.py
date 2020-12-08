#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

res=-1
start_val=[]

with open("input_day8.txt","r") as inp:
	for i in inp:
		start_val.append(i[:-1])


# part 2

def nbr_convert(nbr_str):
	if len(nbr_str)==1:
		nbr=int(nbr_str)
	else:
		nbr=int(nbr_str[1:])
		if nbr_str[0]=="-":
			nbr=-nbr
	return nbr

changed_val_nbr = 1
test=0
val=copy.copy(start_val)

def rec(index, index_done, actions):
	global val
	global test

	if index >= len(val):
		return 0

	if test==1 and index in index_done:
		return -10000000

	value = val[index].split(' ')

	if index in index_done:
		test=1
		cpt=0
		new_index='error'
		new_nbr=0
		while True:
			act = actions[len(actions)-1]
			index_done.pop()
			actions.pop()
			if act[0] == 'jmp':
				cpt+=1
				if cpt==changed_val_nbr:
					new_index=act[2]
					val[act[2]] = 'nop '+str(act[1])
					break
			elif act[0] == 'nop':
				cpt+=1
				if cpt==changed_val_nbr:
					new_index=act[2]
					val[act[2]] = 'jmp '+str(act[1])
					break
			else:
				new_nbr-=act[1]

		return new_nbr+rec(new_index, index_done, actions)


	index_done.append(index)

	number = nbr_convert(value[1])

	actions.append((value[0], number, index))

	if value[0]=='acc':
		return number+rec(index+1, index_done, actions)
	elif value[0]=='jmp':
		return rec(index+number, index_done, actions)
	else:
		return rec(index+1, index_done, actions)


while res<0:
	res=rec(0, [], [])
	changed_val_nbr+=1
	test=0
	val=copy.copy(start_val)

print("part2 :",res)