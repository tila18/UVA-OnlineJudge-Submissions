def calculate(x, y, z):
	return int(round(((x / y) * z) * y))

testcases = int(input())

for testcase in range(testcases):

	sum = 0
	farmers = int(input())

	for farmer in range(farmers):
		i = input().split()

		x = int(i[0])
		y = int(i[1])
		z = int(i[2])

		sum += calculate(x, y, z)

	print(sum)
