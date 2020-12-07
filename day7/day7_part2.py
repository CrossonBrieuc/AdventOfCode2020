#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

def rep(chaine):
	chaine=chaine.replace(","," |").replace("bags","").replace("bag","").replace("contain","").replace("no other","").split(" ")
	x=0
	while x < len(chaine):
		if chaine[x]=="":
			del chaine[x]
		else:
			x+=1
	return chaine

with open("input_day7.txt","r") as inp:
	for i in inp:
		ni=rep(i[:-2])
		val.append(("".join(ni[:2]),"".join(ni[2:])))


# part 2

to_test = 'shinygold'

def find(to_find):
	find_res=0
	for x,y in val:
		if x == to_find:
			if y=='':
				find_res=0
			else:
				for z in y.split('|'):
					find_res+=int(z[0])+int(z[0])*find(z[1:])
			break
	return find_res


res=find(to_test)

print("part2 :",res)