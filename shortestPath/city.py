# 미래도시의 방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표일 때,
# 회사 사이를 이동하게 되는 최소시간 계산, 양방향 이동 가능

INF = int(1e9)

# 노드/간선의 개수 입력
n, m = map(int, input().split())
# 2차원 리스트 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a와 b가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 x와 최종 목적지 노드 k 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:  # 도달할 수 있다면 최단 거리 출력
    print(distance)
