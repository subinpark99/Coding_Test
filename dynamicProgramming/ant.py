# 개미가 정찰병에게 들키지 않기 위해 최소한 한 칸이상 떨어진 일직선상의 식량창고를 약탈하려고 할 때,
# 얻을 수 있는 식량의 최댓값 구하기

# 정수 n 입력
n = int(input())
# 모든 식량 정보 입력
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 상향식 다이나믹 프로그래밍 진행
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
