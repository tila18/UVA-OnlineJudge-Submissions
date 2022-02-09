import sys

def read_num():
    return list(map(int, sys.stdin.readline().split()))

def read_matrix():
    try:
        rows, columns = read_num()
    except ValueError:
        return []   # EOF
    # read all matrix integers into a single list
    numbers = []
    while len(numbers) < rows*columns:
        numbers.extend(read_num())

    # reconstruct matrix
    return [numbers[columns*r:columns*(r+1)] for r in range(rows)]


def optimal_path(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    # shortest path, each cell contains weight for the minimal path
    # to reach the cell followed by the list of rows used by the path.
    sp = [[None for _ in range(number_of_columns)] for _  in range(number_of_rows)]
    for r in range(number_of_rows): # Initialize first column
        sp[r][0] = (matrix[r][0], r+1)
  
    # Construct minimal weight matrix
    for c in range(1, number_of_columns):
        for r in range(number_of_rows):

            # cells from where this cell can be reached (wrapping rows)
            top = sp[(number_of_rows+r-1)%number_of_rows][c-1]
            mid = sp[r][c-1]
            bot = sp[(r+1)%number_of_rows][c-1]

            # best path to reach this cell
            best = min(top, mid, bot)
            
            # add current cell weight to the path weight, and append current row
            sp[r][c] = (best[0] + matrix[r][c],) + best[1:] + (r+1,)

    # find minimal-weight path
    min_weight_path = min(sp[r][-1] for r in range(number_of_rows))
    
    return min_weight_path[0], min_weight_path[1:]


results = []
matrix = read_matrix()

while matrix:
    cost, path = optimal_path(matrix)
    resultstring = str(" ".join(map(str, path)))
    resultstring += "\n" + str(cost)
    results.append(resultstring)
    matrix = read_matrix()

for res in results:
    print(res)