def cross_product(prev, mid, next):
    return (mid[0] - prev[0]) * (next[1] - prev[1]) - (mid[1] - prev[1]) * (next[0] - prev[0])

def check_if_convex(cross1, cross2):
    return True if cross1 * cross2 < 0 else False

results = []

while True:
    n = int(input())

    if n == 0:
        break

    points = []

    for point in range(n):
        line = input().split()
        coordinate = [int(line[0]),int(line[1])] # [x,y]
        points.append(coordinate)

    # first three points
    start_cross = cross_product(points[0], points[1], points[2])

    # critical point if derivate = 0
    convex = True # if the function stops being convex, there is a critical point, as the function flips to being concave, as that creates a point with derivate of 0

    for i in range(2, n-1): # 0,1,2 already done
        # check points[i] and its neighbours
        current_cross = cross_product(points[i-1], points[i], points[i+1])
        # if one of them is negative, the slope has turned, but not both are as that would be inl ine with the function
        if check_if_convex(current_cross, start_cross):
            convex = False
            break

        # check the first point with the last point as its neighbour
        if check_if_convex(cross_product(points[-1], points[0], points[1]), start_cross): 
            convex = False
            
        # check the last point with the first point as its neighbour
        if check_if_convex(cross_product(points[-1], points[0], points[1]), start_cross): 
            convex = False

    results.append("No" if convex else "Yes")

for result in results:
    print(result)