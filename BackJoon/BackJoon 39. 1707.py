import sys
from collections import defaultdict, deque
input = sys.stdin.readline


K = int(input())

for k in range(K):
    V, E = map(int, input().split())
    dict = defaultdict(int)
    Map = defaultdict(list)
    for _ in range(E):
        A, B = map(int, input().split())
        Map[A].append(B)
        Map[B].append(A)
    queue = deque()

    visited = [False for _ in range(V+1)]
    check = True
    for i in range(1, V+1):
        if visited[i]:
            continue
        queue.append(i)
        dict[i] = 1
        visited[i] = True
        while queue and check:
            node = queue.popleft()
            color = dict[node]
            for i in Map[node]:
                if dict[i] == 0:
                    dict[i] = 3-color
                    visited[i] = True
                    queue.append(i)
                elif dict[i] == color:
                    check = False
                    break
                else:
                    continue

    if check:
        print("YES")
    else:
        print("NO")
