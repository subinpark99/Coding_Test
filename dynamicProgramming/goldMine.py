# 1. n x m 크기의 금이 들어있는 금광에서, 첫번째 열부터 출발하여 금을 캐기 시작함
# 2. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있지만, 이후 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야함
# 3. 이때 채굴자가 얻을 수 있는 금의 최대 크기를 출력

# 테스트 케이스 입력
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    for j in range(1, m):  # 열 기준 테이블 갱신
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
