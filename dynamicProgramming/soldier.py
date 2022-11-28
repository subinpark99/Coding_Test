# N명의 병사들을 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치해야 함,
# 또한 배치 과정에서 특정 위치에 있는 병사를 열외시켜야 한다고 할 때
# 남아있는 병사의 수가 최대가 되도록 하기 위해 열외시켜야 하는 병사의 수 출력

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 LIS 문제로 변환
array.reverse()

dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수 출력
print(n - max(dp))
