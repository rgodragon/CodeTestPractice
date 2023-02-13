import copy
N,M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

visited = copy.deepcopy(graph)

for i in range(N):
    for m in range(M):
        visited[i][m] = 0


def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False

    if graph[x][y]==0 and not visited[x][y]:
    # if not visited[x][y] and graph[x][y]==0:
        visited[x][y] = True
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        # print(visited, sep='\n')
        return True
    return False
    
num=0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True :
            num+=1
print(num)

'''
4 5
00110
00011
11111
00000
'''