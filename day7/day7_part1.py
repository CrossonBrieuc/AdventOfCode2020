#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

def rep(chaine):
	chaine=chaine.replace(","," |").replace("bags","").replace("bag","").replace("contain","").split(" ")
	x=0
	while x < len(chaine):
		try:
			int(chaine[x])
			del chaine[x]
		except:
			if chaine[x]=="":
				del chaine[x]
			else:
				x+=1
	return chaine

with open("input_day7.txt","r") as inp:
	for i in inp:
		ni=rep(i[:-2])
		val.append(("".join(ni[:2]),"".join(ni[2:])))


# part 1

to_test = ['shinygold']
lng_save = 0
lng_test = 1
while lng_save<lng_test:
	lng_save=lng_test
	for x,y in val:
		for z in y.split('|'):
			if z in to_test and x not in to_test:
				res+=1
				to_test.append(x)
	lng_test=len(to_test)
	print(lng_test)

print("part1 :",res)