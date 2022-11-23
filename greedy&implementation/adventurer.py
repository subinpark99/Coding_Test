# 모험가 길드에서 N명의 모험가를 대상으로 공포도를 측정 할 때,
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 함
# 이 때 여행을 떠날 수 있는 그룹 수의 최댓값 구하기 (모든 모험가를 특정한 그룹에 넣을 필요는 없음)

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1  # 현재 그룹에 해당 모험가 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 그룹 결성
        result += 1  # 총 그룹 수 증가
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)
