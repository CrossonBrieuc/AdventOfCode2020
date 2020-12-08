#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input_day8.txt","r") as inp:
	for i in inp:
		val.append(i[:-1])

# part 1

def nbr_convert(nbr_str):
	nbr=int(nbr_str[1:])
	if nbr_str[0]=="-":
		nbr=-nbr
	return nbr

def rec(index, index_done):
	value = val[index].split(' ')
	number = nbr_convert(value[1])

	if index in index_done:
		return 0
	index_done.append(index)


	if value[0]=='acc':
		return number+rec(index+1, index_done)
	elif value[0]=='jmp':
		return rec(index+number, index_done)
	else:
		return rec(index+1, index_done)

	
acc=rec(0, [])


print("part1 :",acc)