# 파이썬 이진 탐색 라이브러리
# 값이 특정 범위에 속하는 데이터 개수 구하기

from bisect import bisect_right, bisect_left

def count(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count(a, 4, 4))
# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count(a, -1, 3))
