#!/usr/bin/env python
# -*- coding: utf-8 -*-

res=0
nbr_inter = []
my_ticket = []
other_ticket = []

with open("input.txt","r") as inp:
	i2=0
	for i in inp:
		if i == '\n':
			i2+=1
		elif i2==0:
			nbr_inter.append(i[:-1])
		elif i2==1:
			my_ticket.append(i[:-1])
		elif i2==2:
			other_ticket.append(i[:-1])


# part 1

valid_nbr = []

for x in nbr_inter:
	for y in x.split(' '):
		try:
			int(y[0])
			y = [int(i) for i in y.split('-')]
			for z in range(y[0],y[1]+1):
				valid_nbr.append(z)
		except:
			continue


unvalid_ticket = []
unvalid_ticket_id = []

for nb,x in enumerate(other_ticket[1:]):
	x = [int(i) for i in x.split(',')]
	for y in x:
		if y not in valid_nbr:
			unvalid_ticket.append(y)
			unvalid_ticket_id.append(nb)

unvalid_ticket_id.sort()

res = sum(unvalid_ticket)

print("part1 :", res)


# part 2


classed_valid_nbr = []

for nb,x in enumerate(nbr_inter):
	classed_valid_nbr.append([])
	for y in x.split(' '):
		try:
			int(y[0])
			y = [int(i) for i in y.split('-')]
			for z in range(y[0],y[1]+1):
				classed_valid_nbr[nb].append(z)
		except:
			continue



other_ticket.append(my_ticket[1])

classed_ticket_nbr = [[] for i in range(len(my_ticket[1].split(',')))] 

for nb1,x in enumerate(other_ticket[1:]):
	if nb1 in unvalid_ticket_id:
		continue
	else:
		x = [int(i) for i in x.split(',')]
		for nb2,y in enumerate(x):
			classed_ticket_nbr[nb2].append(y)



couple = [[] for i in range(len(my_ticket[1].split(',')))] 

for nb1,x in enumerate(classed_valid_nbr):
	for nb2,y in enumerate(classed_ticket_nbr):
		test = True
		for z in y:
			if z not in x:
				test = False
				break
		if test:
			couple[nb1].append(nb2)
			

done = []

def delter():
	global couple
	global done

	for x in couple:
		if len(x) == 1 and x[0] not in done:
			nbr = x[0]
			done.append(nbr)
			break
	
	test = False
	for i,x in enumerate(couple):
		if nbr in x and len(x)>1:
			couple[i].remove(nbr)
			test = True

	return test
			
test2 = True
while test2:
	test2 = delter()


res2 = 1

my_ticket_nbr = [int(i) for i in my_ticket[1].split(',')]

for i in range(6):
	res2 *= my_ticket_nbr[couple[i][0]]

print("part2 :",res2)