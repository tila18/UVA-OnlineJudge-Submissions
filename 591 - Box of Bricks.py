sets = []

while True:
	n = int(input())
	moves = 0

	if n > 0:
		stacks = input().split()
		stacks = [int(i) for i in stacks]
		stacks.sort(reverse=True)
		sumstacks = sum(stacks)
		height = sumstacks / n
		x=0
	
		while x < n: # while looking at stacks (index 0-5)
			if stacks[x] > height:	
				for y in range(x+1, n):
					if stacks[y] < height:
						stacks[y] += 1
						stacks[x] -= 1
						moves += 1
						break
			else:
				x += 1 # look at next one
				
		sets.append(moves)

	else:
		break

set_counter = 1

for set in sets:
	print('Set #' + str(set_counter))
	print('The minimum number of moves is ' + str(set) +'.')
	print()
	set_counter += 1