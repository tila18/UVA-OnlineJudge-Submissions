import math
import sys

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

def dist(p1, p2):
	return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

# brute force method to return the smallest distance between two points in list
def brute_force_min_dist(P, n):
	min_val = 40000
	for i in range(n):
		for j in range(i + 1, n):
			if dist(P[i], P[j]) < min_val:
				min_val = dist(P[i], P[j])

	return min_val

# find the distance between the closest points of strip[] of given size, points sorted on y upper bound on minimum distance as d.
# Note that this method seems to be a O(n^2) method, but it's a O(n) method as the inner loop runs at most 6 times (plane sweep)
def stripClosest(strip, size, d):
	
	min_val = d

	# for all points try the next points until the difference between y coordinates < d. (at most 6 times)
	for i in range(size):
		j = i + 1
		while j < size and (strip[j].y - strip[i].y) < min_val:
			min_val = dist(strip[i], strip[j])
			j += 1

	return min_val

# recursive function to find the smallest distance between points sorted on x
def closest_points(P, Q, n):
	
	# if there are 2 or 3 points -> brute force
	if n <= 3:
		return brute_force_min_dist(P, n)

	# find the middle point
	mid = n // 2
	midPoint = P[mid]

	#keep a copy of left and right branch
	Pl = P[:mid]
	Pr = P[mid:]

	# mimicing a vertical line passing through the middle point, calculate the smallest distance dl = left of middle point and dr = right of middle point (plane sweep)
	dl = closest_points(Pl, Q, mid)
	dr = closest_points(Pr, Q, n - mid)

	# find the smaller of two distances
	d = min(dl, dr)

	# build a list that contains points close (closer than d) to the line passing through the middle point
	stripP = []
	stripQ = []
	lr = Pl + Pr
	for i in range(n):
		if abs(lr[i].x - midPoint.x) < d:
			stripP.append(lr[i])
		if abs(Q[i].x - midPoint.x) < d:
			stripQ.append(Q[i])

	stripP.sort(key = lambda point: point.y) 
	min_a = min(d, stripClosest(stripP, len(stripP), d))
	min_b = min(d, stripClosest(stripQ, len(stripQ), d))
	
	# return the minimum of d and self.closest
	return min(min_a,min_b)


# finds the smallest distance by calling closest_points() recursively
def closest_rec(P, n):
	P.sort(key = lambda point: point.x)
	Q = P
	Q.sort(key = lambda point: point.y)

	return closest_points(P, Q, n)


results = []

with sys.stdin as input:
	while True:
		try:
			points_in_case = input.readline()
			if int(points_in_case) == 0:
				break
			else:
				case = []
				for p in range(int(points_in_case)):
					point = input.readline().split()
					case.append(Point(int(point[0]), int(point[1])))
			
				result = closest_rec(case, len(case))
				if result < 10000:
					results.append(str("%.4f" % result))
				else:
					results.append("INFINITY")
		except EOFError:
			break

for res in results:
	print(res)

sys.exit(0)