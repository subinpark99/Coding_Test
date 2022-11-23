# N과 K가 주어질 때 N이 1이 될 때까지
# N에서 1을 빼거나 N을 K로 나누는 과정을 수행 해야 하는 최소 횟수 구하기

# 내 풀이
n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n = n // k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)


# 해답
a, b = map(int, input().split())

result = 0

while True:
    # a가 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (a // b) * b
    result += (a - target)
    a = target

    # a가 b보다 작을 때 반복문 탈출
    if a < b:
        break
    result += 1
    a //= b

result += (a - 1)
print(result)
