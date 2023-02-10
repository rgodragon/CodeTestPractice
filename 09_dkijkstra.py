### 다익스트라 알고리즘

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# #print(INF)

# n, m = map(int, input().split())
# # graph = [list(map(int, input().split())) for _ in range(M)]
# start = int(input())
# graph = [[] for i in range(n + 1)]

# # x, k = map(int, input().split())

# visited = [False] * (n + 1)
# distance = [INF] * (n + 1)

# # graph = [[] for i in range(M + 1)]
# # print(N, M)
# # print(X, K)

# #모든 간선 정보를 입력받기
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     # c = 1
#     graph[a].append((b, c))

# # print(graph)

# #방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#             # print(index, distance[i])
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     # print(graph[start])
#     for j in graph[start]:
#         distance[j[0]] = j[1]  # 스타트 노드부터 갈 수 있는 노드까지 거리 매겨두기
#     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(n - 1):
#         #최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
#         now = get_smallest_node()
#         # print(now)
#         visited[now] = True
#         #현재 노드와 연결된 다른 노드 확인
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             # 현재 노들르 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#         # print(distance)

#         # print(now)

# #     for i in range(N - 1):  # 시작 노드 제외
# #         now = get_smallest_node()
# #         print('now', now)
# #         visited[now] = True
# #     # 현재 노드와 연결된 다른 노드를 확인
# #         for j in graph[now]:
# #           cost = distance[now] +

# dijkstra(start)

# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

############# heapq 연습ß
# import heapq
# # 오름차순 힙 정렬

# def heapsort(iterable):
#     h = []
#     result = []
#     # 모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h, value)
#         # 힙에 삽입된 모든 원소를 차레대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result

# result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
# print(result)

################## 미래 도시
# import sys

# input = sys.stdin.readline
# N, M = map(int, input().split())

# INF = int(1e9)
# graph = [[] for i in range(N + 1)]
# visited = [False] * (N + 1)
# distance = [INF] * (N + 1)

# #모든 간선 정보를 입력받기
# for _ in range(M):
#     a, b = map(int, input().split())
#     c = 1
#     graph[a].append((b, c))

# X, K = map(int, input().split())

# # print(N, M)
# # print(graph)

# # print(X, K)

# # # print(graph)

# #방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, N + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#             # print(index, distance[i])
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     # print(graph[start])
#     for j in graph[start]:
#         distance[j[0]] = j[1]  # 스타트 노드부터 갈 수 있는 노드까지 거리 매겨두기
#     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(N - 1):
#         #최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
#         now = get_smallest_node()
#         # print(now)
#         visited[now] = True
#         #현재 노드와 연결된 다른 노드 확인
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             # 현재 노들르 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#         # print(distance)

# dijkstra(1)
# toK = distance[K]
# # print(distance[K])

# dijkstra(K)
# toX = distance[X]

# if (toK + toX < 1e9):
#     print(toK + toX)
# else:
#     print(-1)

# for i in range(1, N + 1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

################## 전보
# import sys

# input = sys.stdin.readline
# N, M, C = map(int, input().split())

# INF = int(1e9)
# graph = [[] for i in range(N + 1)]
# visited = [False] * (N + 1)
# distance = [INF] * (N + 1)

# #모든 간선 정보를 입력받기

# for _ in range(M):
#     X, Y, Z = map(int, input().split())
#     graph[X].append((Y, Z))

# # X, K = map(int, input().split())

# # print(N, M)
# # print(graph)

# # print(X, K)

# # # print(graph)

# #방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, N + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#             # print(index, distance[i])
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     # print(graph[start])
#     for j in graph[start]:
#         distance[j[0]] = j[1]  # 스타트 노드부터 갈 수 있는 노드까지 거리 매겨두기
#     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(N - 1):
#         #최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
#         now = get_smallest_node()
#         # print(now)
#         visited[now] = True
#         #현재 노드와 연결된 다른 노드 확인
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             # 현재 노들르 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#         # print(distance)

# dijkstra(C)
# print(distance)

# cityNum = 0
# maxTime = 0
# for i in distance:
#     if i != 0 and i != 1e9:
#         cityNum += 1
#         maxTime = max(maxTime, i)

# print(cityNum, maxTime)

# ################## heaq 예시

# import heapq
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n + 1)]
# distance = [INF] * (n + 1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))  #튜플로 저장

# def dijkstra(start):
#     q = []  #우선순위 스택
#     heapq.heappush(q, (0, start))  # q:  여기에 넣겟다, (0,start) 거리 노드
#     # print(q)
#     distance[start] = 0
#     while q:  #큐가 비어있지 않다면
#         dist, now = heapq.heappop(q)  # 넣은 튜플
#         # print(dist, now)
#         if distance[now] < dist:  # 가려고 노드의 거리가 INF가 아닐때 -> 처리한 노드일때
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]  # 새로가려고 하는 거리
#             if cost < distance[i[0]]:  # 기존 거리보다 새 거리가 더 짧으면
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(start)
# print(distance)

################## heaq 이용 전보

# import heapq
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# N, M, C = map(int, input().split())
# # start = int(input())
# graph = [[] for i in range(N + 1)]
# distance = [INF] * (N + 1)

# for _ in range(M):
#     X, Y, Z = map(int, input().split())
#     graph[X].append((Y, Z))  #튜플로 저장

# def dijkstra(start):
#     q = []  #우선순위 스택
#     heapq.heappush(q, (0, start))  # q:  여기에 넣겟다, (0,start) 거리 노드
#     # print(q)
#     distance[start] = 0
#     while q:  #큐가 비어있지 않다면
#         dist, now = heapq.heappop(q)  # 넣은 튜플
#         # print(dist, now)
#         if distance[now] < dist:  # 가려고 노드의 거리가 INF가 아닐때 -> 처리한 노드일때
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]  # 새로가려고 하는 거리
#             if cost < distance[i[0]]:  # 기존 거리보다 새 거리가 더 짧으면
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(C)
# # print(distance)

# cityNum = 0
# maxTime = 0
# for i in distance:
#     if i != 0 and i != 1e9:
#         cityNum += 1
#         maxTime = max(maxTime, i)

# print(cityNum, maxTime)

# ##############플루이드 워셜

# INF = int(1e9)

# #노드의 개수 및 간선
# n, m = map(int, input().split())

# # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# # print(*graph, sep='\n')

# # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# # print(*graph, sep='\n')

# # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# # 점화식에 따라 플로이드 워셜 알고리즘 수행
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print(*graph, sep='\n')

##############  미래도시 - 플루이드 워셜 이용

INF = int(1e9)

#노드의 개수 및 간선
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# print(*graph, sep='\n')

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# print(*graph, sep='\n')

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    c = 1
    graph[a][b] = c
    graph[b][a] = c

x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if (graph[1][k] + graph[k][x] < INF):
    print(graph[1][k] + graph[k][x])
else:
    print(-1)

# print(*graph, sep='\n') 
