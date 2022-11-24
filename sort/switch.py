# N,K 그리고 배열 A,B 가 주어졌을 때,
# 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력

n, k = map(int, input().split())  # 원소 개수 N과 최대 바꿔치기 연산 횟수 K 입력 받기
a = list(map(int, input().split()))  # 배열 A의 모든 원소 입력 받기
b = list(map(int, input().split()))  # 배열 B의 모든 원소 입력 받기

a.sort()  # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True)  # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출
    else:
        break
print(sum(a))  # 배열 A의 모든 원소의 합 출력
