# N개의 원소를 포함하는 수열이 오름차순으로 정렬되어 있을 때,
# 이 수열에서 x가 등장하는 횟수 계산하기

from bisect import bisect_left, bisect_right


def count(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x,x] 범위에 있는 데이터의 개수 계산
counts = count(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if counts == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(counts)
