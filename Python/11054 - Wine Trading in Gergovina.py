import sys

with sys.stdin as input:

    while True:
        n = int(input.readline())
        if n == 0: # 2 <= n <= 100 000
            break
    
        a_list = input.readline().split()
        a_list = list(map(int, a_list))
    
        ans, last = 0, 0
    
        for a in a_list:
            last += a
            ans += abs(last)
        
    
        sys.stdout.write(str(ans) + '\n')