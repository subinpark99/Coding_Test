# 정수 x가 주어졌을 때, 연산 4개를 적절히 사용해서 1로 만들기, 연산을 사용하는 횟수의 최솟값 출력
# 1. x가 5로 나누어 떨어지면, 5로 나눔
# 2. x가 3으로 나누어 떨어지면, 3으로 나눔
# 3. x가 2로 나누어 떨어지면, 2로 나눔
# 4. x에서 1을 뺌

x = int(input())
d = [0] * 30001

for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])