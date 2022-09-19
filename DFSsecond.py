from collections import deque

#n,m입력
n, m = map(int, input().split())
graph = []

#그래프 입력
for _ in range(n):
    graph.append(list(map(int, input())))

# print(n, m)
# print(graph)

result = 0


def dfs(x, y):

    #범위 벗어나면 False
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    #지금 좌표 안 갔던 곳인지 확인
    if graph[x][y] == 0:
        # 간 곳으로 만들기
        graph[x][y] = 1
        #상,하,좌,우 이동하며 연결 체크 - 아래 다 아닌 경우에 True 하나 내보내기
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j): result += 1

print(result)
