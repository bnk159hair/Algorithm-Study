import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    Map = [False, defaultdict(list), False]
    check = True
    for n in range(N):
        num = input()[:-1]
        cur = Map
        if check:
            for i in range(len(num)+1):
                if cur[0]:
                    check = False
                    break
                if i == len(num):
                    cur[0] = True
                    if cur[2]:
                        check = False
                    break
                cur[2] = True
                if len(cur[1][num[i]]) == 0:
                    cur[1][num[i]] = [False, defaultdict(list), False]
                cur = cur[1][num[i]]

    if check:
        print("YES")
    else:
        print("NO")
