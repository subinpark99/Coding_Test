# 500원, 100원, 50원, 10원 단위의 동전 거슬러 주기

n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin  # 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
