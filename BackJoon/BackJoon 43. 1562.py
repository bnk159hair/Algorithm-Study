# 실패 코드
# import sys

# input = sys.stdin.readline

# N = int(input())

# result = 0


# def Find(depth, bit, b_num):
#     global result
#     if depth == N:
#         for i in range(10):
#             if not bit & (1 << i):
#                 return
#         result += 1
#         return
#     cnt = 0
#     for i in range(10):
#         if not bit & (1 << i):
#             cnt += 1
#     if N-depth < cnt:
#         return
#     if b_num == 0:
#         Find(depth+1, bit | 1, 1)
#     elif b_num == 9:
#         Find(depth+1, bit | (1 << 8), 8)
#     else:
#         Find(depth+1, bit | (1 << b_num-1), b_num-1)
#         Find(depth+1, bit | (1 << b_num+1), b_num+1)


# for i in range(1, 10):
#     Find(1, 1 << i, i)

# print(result % 1000000000)

# https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-1562%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%88%98
import sys

input = sys.stdin.readline

Max = (1 << 10) - 1

N = int(input())


def Find():
    dp = [[0]*(Max+1) for _ in range(10)]

    for i in range(1, 10):
        dp[i][1 << i] = 1

    for _ in range(2, N+1):
        next_dp = [[0]*(Max+1) for _ in range(10)]

        for i in range(10):
            for j in range(Max+1):
                if i > 0:
                    next_dp[i][j | (1 << i)] = (
                        next_dp[i][j | (1 << i)] + dp[i-1][j]) % 1000000000
                if i < 9:
                    next_dp[i][j | (1 << i)] = (
                        next_dp[i][j | (1 << i)] + dp[i+1][j]) % 1000000000
        dp = next_dp

    return sum(dp[i][Max] for i in range(10)) % 1000000000


print(Find())
