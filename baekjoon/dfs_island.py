w,h = map(int, input().split())
result=[]

while w!=0 and h!=0:
    graph=[]
    num=0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    def dfs(x,y):
        if x<0 or x>=h or y<0 or y>=w:
            return False
        if graph[x][y]==1:
            graph[x][y]=0
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y+1)
            dfs(x+1,y-1)
            dfs(x-1,y+1)
            dfs(x-1,y-1)
            return True
        return False
    
    # print(graph)
    for i in range(w):
        for j in range(h):
            if dfs(i,j) :
                num+=1
    result.append(num)
    w,h = map(int, input().split())

for i in result:
    print(i)

'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
'''