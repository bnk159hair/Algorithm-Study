import sys
import bisect

# 냅색 문제 - N개의 물건이 있을 때
# 브루트포스 로 하면 2^N이 됌
# N이 커지면 시행시간이 너무 오래 걸림

input = sys.stdin.readline

N, C = map(int, input().split())
bag = list(map(int, input().split()))


def bitmasking(arr):  # 비트 마스킹으로 모든 경우의 수 탐색
    result = []
    for i in range(1 << len(arr)):  # arr 길이 만큼 옮기기 00, 01, 10, 이런식으로 모든 경우의 수 확인 가능
        Sum = 0
        for j in range(len(arr)):
            if ((1 << j) & i) != 0:  # 각각의 경우의 수에 대한 합 구하기
                Sum += arr[j]
        result.append(Sum)
    return result


if N == 1:
    if bag[0] <= C:
        print(2)
    else:
        print(1)
else:
    # 그래서 배열을 두 개로 나누고 시작 (2^(N/2))
    arr1 = bag[:N//2]
    arr2 = bag[N//2:]
    front_arr = bitmasking(arr1)
    back_arr = bitmasking(arr2)
    back_arr.sort()
    result = 0
    for i in range(len(front_arr)):
        result += bisect.bisect_right(back_arr, C-front_arr[i])
    print(result)
