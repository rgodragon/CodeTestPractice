import copy
N,M = map(int, input().split())
graph = []


for _ in range(N):
    graph.append(list(map(int, input())))
visited = copy.deepcopy(graph)

for i in range(N):
    for j in range(M):
        visited[i][j]=0

    # for j in range(M):
    #     visited[i].append(0)

print(graph, sep='\n')
print(visited, sep='\n')


num=0
def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M :
        return False

    # 현재 노드 아직 방문하지 않았다면
    if not visited[x][y] and graph[x][y]==0:
        visited[x][y]=True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

num=0
for i in range(N):
    for j in range(M):
        if dfs(i,j):
            num+=1

print(num)

# print(graph[0][0])
# print(graph[1][1])


# num = 0

# def dfs(graph, v, visited):
#     visited[v]=True
#     for i in graph[v]:
#         if not visited[i]:
#             if graph[v]==0:
#                 dfs(graph, i, visited)
#             else :
#                 num+=1
# # 각 노드가 방문된 정보를 리스트 자료형으로 표현 - 1차원 리스트




# 입력 예시
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000000111000
11111111110011
11100011111111
11100011111111
'''
