import sys

""" recursively called to substitute 0 with its submobile"""
def sub_mob(mobile):

    if mobile and isinstance(mobile[0], int):
        if mobile[0] == 0: #left child
            mobile[0] = calc_weights(sub_mob(inputlist.pop(0)))
            
    if mobile and isinstance(mobile[2], int):
        if mobile[2] == 0: #right child
            mobile[2] = calc_weights(sub_mob(inputlist.pop(0)))
            
    return mobile

""" substitute nested lists with its submobile's weight"""
def calc_weights(mobile):
        
    if mobile[0] * mobile[1] != mobile[2] * mobile[3]:
        return mobile    
    else:    
        return mobile[0] + mobile[2]    
         

results = []
counter = 0
cases = int(input())
blankline = input()

with sys.stdin as input:
    inputlist = []

    while counter < cases:
        line = input.readline().split()
        
        # blank line ends a case
        if len(line) == 0:

            tree = []
            tree = sub_mob(inputlist.pop(0))
            results.append(tree)      

            counter += 1
            case_list = []

        else:
            inputlist.append([int(i) for i in line])

print_count = 0
for x in results:
    for y in x:
        if isinstance(y, int) == False:
            break

    if len(x) == 4 and x[0]*x[1] == x[2]*x[3]:
        sys.stdout.write("YES" + '\n')
    else:
        sys.stdout.write("NO" + '\n')
    
    print_count += 1
    if print_count < len(results):
        sys.stdout.write('\n')