# N가지 종류의 화폐가 있을 때, M원을 만들기 위한 최소한의 화폐 개수 출력

# 정수 n,m 입력 받기
n, m = map(int, input().split())

# n개의 화폐 단위 정보 입력
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):  # i는 화폐 단위
    for j in range(array[i], m + 1):  # j는 각각의 금액
        if d[j - array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
