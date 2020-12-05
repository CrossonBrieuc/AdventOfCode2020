
res=0
val=[]

with open("input_day5.txt","r") as input:
	for i in input:
		val.append(i)


# part 1

id_list=[]

for instruction in val:
	row=[0,127]
	col=[0,7]

	for x in instruction[:7]:
		cut=(row[1]-row[0])//2
		if x=='B':
			row[0]+=cut+1
		else:
			row[1]-=cut+1

	row=row[0]

	for x in instruction[7:]:
		cut=(col[1]-col[0])//2
		if x=='R':
			col[0]+=cut+1
		else:
			col[1]-=cut+1

	col=col[0]

	id=row*8+col
	id_list.append(id)

res=max(id_list)

print("part1 :",res)

# part 2

missing_seat=[]

last_id=min(id_list)

id_list.sort()

for id in id_list:
	dif=id-last_id

	if dif>1:
		missing_seat.append(id-1)

	last_id=id

print("part2 :",missing_seat)


