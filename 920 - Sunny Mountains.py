import math

results = []
c = int(input()) #cases

for case in range(c):
    n = int(input()) #coordinate pairs
    points = []

    for pair in range(n):
        line = input().split()
        coordinate = [int(line[0]),int(line[1])] # [x,y]
        points.append(coordinate)

    points.sort() #to build the mountain like the picture, ordered on the x-axis for correct heights of the neighbouring peak

    total = 0 #total length of sunny sides
    max_height = 0 #peaks with x-coordinates less than the max peak will not have sunny sides

    for i in range(len(points)-2,-1,-1): #loops from the last peak -> first point index

        # if point is higher than visited highest peak
        if points[i][1] > max_height:

            #length of current side from [current x,y] to [current x+1, that points y] # vector length = sqrt(|x^2| + |y^2|)
            vector_length = math.sqrt((points[i][0] - points[i+1][0])**2  +(points[i][1] - points[i+1][1])**2)
            sunny_side = vector_length * (points[i][1] - max_height) / (points[i][1] - points[i+1][1])

            total += sunny_side
            max_height = points[i][1]

    results.append("%.2f" % total)

for result in results:
    print(result)