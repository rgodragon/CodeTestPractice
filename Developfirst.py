N = int(input())
routes = input().split()

#print(routes)

X = 1
Y = 1

for route in routes:
    if (route == 'D' and X != N): X += 1
    if (route == 'U' and X != 1): X -= 1
    if (route == 'R' and Y != N): Y += 1
    if (route == 'L' and Y != 1): Y -= 1

print(X, Y)

### 풀이

#입력받기
n=int(input())
x, y = 1,1
movePlans=input().split()

dx = [0, 0, -1 , 1] # 행(세로로 몇번째 행)
dy = [-1,1, 0, 0] # 열(가로로 몇번째 열)
moveTypes=['L','R','U','D']

for movePlan in movePlans:
  for i in range(len(moveTypes)):
    if movePlan == moveTypes[i]:
      nx = x + dx[i] # 가려고 하는 방향
      ny = y + dy[i]
  # 예외 사항 제외
  if nx <1 or ny<1 or nx>n or ny >n:
    continue # 컨티뉴로 밑에 코드 무시하기
    
  x, y = nx, ny

print(x,y)


