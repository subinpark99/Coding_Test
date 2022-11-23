# 각 자리가 숫자(0-9)로만 이루어 진 문자열 S가 주어졌을 때,
# 왼쪽부터 오른쪽으로 숫자 사이에 ‘x’ 혹은 ‘+’ 연산자를 넣어 만들 수 있는 가장 큰 수 구하기

# 내 풀이
p = input()

answer = 0
for i in p:
    if int(i) <= 0 or answer <= 0:
        answer += int(i)
    else:
        answer *= int(i)
print(answer)


# 해답
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0이나 1이면 더하기
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
