import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def find(x):
    if arr[x][0] == x:
        return arr[x][0]

    arr[x][0] = find(arr[x][0])

    return arr[x][0]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return arr[px][1]
    if px < py:
        arr[py][0] = px
        arr[px][1] += arr[py][1]
        return arr[px][1]
    else:
        arr[px][0] = py
        arr[py][1] += arr[px][1]
        return arr[py][1]


T = int(input())
for i in range(T):
    F = int(input())
    arr = {}
    for j in range(F):
        a, b = input().split()
        if not a in arr:
            arr[a] = [a, 1]
        if not b in arr:
            arr[b] = [b, 1]
        print(union(a, b))
