# 알파벳 대문자와 숫자(0-9)로만 구성된 문자열을 입력했을 때,
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력

data = input()
result = []
value = 0

for x in data:
    # 알파벳인 경우 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 존재하면 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 리스트를 문자열로 변환하여 출력
print(''.join(result))
