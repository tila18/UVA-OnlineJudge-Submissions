import sys

def create_matrix():
    max_n = 101
    max_k = 101
    matrix = [[0]*(max_n) for x in range(max_k)] # index 0 to 100 in 2 dimensions
    
    for i in range(max_n):
        matrix[1][i] = 1
        for i in range(max_k):
            matrix[i][0] = 1
      
        for k in range(2, max_k):
            for n in range(1, max_n):
                matrix[k][n] = sum(matrix[k-1][:n+1]) % 1000000
    return matrix


matrix = create_matrix()

with sys.stdin as input:
    while True:
        line = input.readline().split()
        n = int(line[0])
        k = int(line[1])
    
        if n == k == 0:
            break
    
        sys.stdout.write(str(matrix[k][n]) + '\n')