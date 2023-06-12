import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

parent = [i for i in range(201)]


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


N = int(input())
M = int(input())

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] != 0:
            union(i+1, j+1)

arr = list(map(int, input().split()))
check = True
for i in range(1, len(arr)):
    if not isUnion(arr[i-1], arr[i]):
        print("NO")
        check = False
        break

if check:
    print("YES")
