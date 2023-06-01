import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

parent = [i for i in range(1000001)]


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return
    if px < py:
        parent[py] = px
    else:
        parent[px] = py


def isUnion(x, y):
    px = find(x)
    py = find(y)

    return px == py


n, m = map(int, input().split())

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        if isUnion(a, b):
            print("YES")
        else:
            print("NO")
