'''
Title     : Security Bijective Functions
Subdomain : Functions
Domain    : Security
Author    : Kalpak Seal
Created   : 24 September 2016
'''
def isBijective(n, l):
    for i in range(0, n):
        for j in range(0, i):
            if (j + 1) in l:
                continue
            else:
                return ("NO")
    return ("YES")

n = int(input())
l = list(map(int, raw_input().split()))

print(isBijective(n, l))