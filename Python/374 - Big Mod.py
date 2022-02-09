import sys

tests = []

with sys.stdin as input:
    while True:
        line = input.readline()
        if line == "":
            break
        
        b = int(line)
        p = int(input.readline())
        m = int(input.readline())

        input.readline()

        answer = pow(b, p, m)
        sys.stdout.write(str(answer) + '\n')   

    sys.stdout.write(" ")