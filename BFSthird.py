from collections import deque

#n,m입력
n, m = map(int, input().split())
graph = []

#그래프 입력
for _ in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]

result = 0

def bfs(x, y):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x,y)) #?
  num = 0

  #큐가 빌 때까지 반복
  while queue :
    num+=1
    print(num, queue)
    x, y = queue.popleft() # 0,0 #1,0 #0,0 #1,2
    for i in range(4):
      nx = x + dx[i]  
      ny = y + dy[i]  # 1,0 #0,0 1,1 # (0,2) (2,2) (1,1), (1,3)
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx <0 or ny <0 or nx>=n or ny>=m:
        continue
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해동 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1: # 2가 되어서 세번쨰 0,0이 못옴.
        graph[nx][ny]  = graph[x][y]+1 # 2
        queue.append((nx,ny)) # 1,0 #0,0 1,1
        print('current ', graph[nx][ny])

  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

#BFS를 수행한 결과 출력
print(bfs(0,0))
  