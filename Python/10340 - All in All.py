import sys

def split(word):
    return [char for char in word]

def containsAll(sub_str, str):
    #return 0 not in [c in sub_str for c in str]
    str_list = split(str)
    sub_str_list = split(sub_str)
    
    for c in str_list:
        if len(sub_str_list) != 0 and c == sub_str_list[0]:
            sub_str_list.pop(0)

    if len(sub_str_list) > 0:
        return 0
    else:
        return 1

with sys.stdin as input:

    while True:
        line = input.readline().split()
        if len(line) == 0:
            break

        if containsAll(line[0], line[1]):
            sys.stdout.write("Yes" + '\n')
        else:
            sys.stdout.write("No" + '\n')