# 매 단계마다 1차원 테이블의 모든 원소를 확인

import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

n, m = map(int, input().split())  # 노드의 개수, 간선의 개수 입력
start = int(input())  # 시작 노드 번호 입력

graph = [[] for i in range(n + 1)]  # 각 노드에 연결돼 있는 노드에 대한 정보를 담는 리스트 생성
visited = [False] * (n + 1)  # 방문한 적이 있는지 체크하는 목적의 리스트 생성
distance = [INF] * (n + 1)  # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a번 노드에서 b번 노드로 가는 비용이 c


# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드 (인덱스)

    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0  # 시작 노드에 대해 초기화
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
    for i in range(n - 1):
        now = get_smallest_node()  # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)  # 다익스트라 알고리즘 수행

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:  # 도달할 수 없는 경우
        print('INFINITY')
    else:  # 도달할 수 있는 경우 거리 출력
        print(distance[i])