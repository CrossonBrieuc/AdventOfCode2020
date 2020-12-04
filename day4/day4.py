#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
val=[]

with open("input_day4.txt","r") as input:
	wait=''
	for i in input:
		i=i[:-1]
		if i=='':
			val.append(wait[:-1])
			wait=''
		else:
			wait+=i+' '
	val.append(wait[:-1])
			

valid_val=[]

# part 1

for x in val:
	x=x.split(' ')

	info_nbr=0

	for y in x:
		y=y.split(':')
		if y[0]!="cid":
			info_nbr+=1

	if info_nbr==7:
		valid_val.append(x)
		res+=1

print("part1 :",res)


# part 2

res=0

spec={
	"byr":[1920,2002],
	"iyr":[2010,2020],
	"eyr":[2020,2030],
	"hgt":{
		"cm":[150,193],
		"in":[59,76]
	},
	"ecl":'amb blu brn gry grn hzl oth'.split(' ')
}


for x in valid_val:
	is_valid=0
	for y in x:
		y=y.split(':')
		if y[0]!="cid":
			try:
				sp=spec[y[0]]
				if y[0]=="hgt":
					try:
						sp2=sp[y[1][-2:]]
						if sp2[0]<=int(y[1][:-2])<=sp2[1]:
							is_valid+=1
					except:1
				elif y[0]=="ecl" and y[1] in sp:
					is_valid+=1
				elif sp[0]<=int(y[1])<=sp[1]:
					is_valid+=1
			except:
				if y[0]=="pid" and len(y[1])==9:
					try:
						int(y[1])
						is_valid+=1
					except:1
				elif y[0]=="hcl" and "#" in y[1] and len(y[1])==7:
					test=True
					for lt in y[1][1:]:
						if 97>ord(lt)>57 or ord(lt)>102 or 48>ord(lt):
							print(lt)
							test=False
							break
					if test:
						is_valid+=1

	if is_valid==7:
		res+=1

print("part2 :",res)

