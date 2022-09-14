x_axis, y_axis = map(int, input().split())
x_pos, y_pos, direction = map(int, input().split())
mapCode = [list(map(int, input().split())) for _ in range(y_axis)]

#directions = [0, 1, 2, 3]  #북 동 남 서

current_pos = [x_pos, y_pos]
current_direction = direction
previous_pos = []
previous_pos.append(current_pos)
oceanFlag = False
previousFlag = False

directions = [0, 3, 2, 1]
dirNum = 0

#전진 횟수
stepCount = 1

#연속 회전 가능 남은 횟수
rotationNum = 4

while (rotationNum > 0):

    # 한스텝 돌기
    dirNum += 1
    if (dirNum > 3): dirNum = 0

    # 가려는 방향 확인
    if (directions[dirNum] == 0):
        heading_pos = [current_pos[0], current_pos[1] - 1]
    if (directions[dirNum] == 1):
        heading_pos = [current_pos[0] + 1, current_pos[1]]
    if (directions[dirNum] == 2):
        heading_pos = [current_pos[0], current_pos[1] + 1]
    if (directions[dirNum] == 3):
        heading_pos = [current_pos[0] - 1, current_pos[1]]

    #print('now in :', current_pos, 'going to :', heading_pos)
    #print('heading position : ', mapCode[heading_pos[1]][heading_pos[0]])

    # 바다인지 확인
    if mapCode[heading_pos[1]][heading_pos[0]]:
        oceanFlag = True
        #print('oceanFlag =', oceanFlag)

# 갔던 곳인지 확인
    if heading_pos in previous_pos:
        previousFlag = True
        #print('previousFlag =', previousFlag)

# 둘 다 아니면 전진
    if oceanFlag != True and previousFlag != True:
        #print('oneStepAhead')
        stepCount += 1
        current_pos = heading_pos
        previous_pos.append(current_pos)
        rotationNum = 4

# 그 회전이 4번이상 반복되면 코드 종료
    else:
        rotationNum -= 1
        oceanFlag = False
        previousFlag = False
        #print('previousVisit =', previous_pos)

    #print('rotationNum =', rotationNum)

print(stepCount)



### 풀이

n,m = map(int, input().split())
x, y, direction = map(int, input().split())
map_code = [list(map(int, input().split())) for _ in range(n)]

visited_map = [[0] * m for _ in range(n)]
visited_map[x][y]=1
#print(visited_map)

#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction 
  direction -=1
  if direction <0 : direction = 3  

count = 1
turn_time=4

while (turn_time > 0):
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  # print(nx, ny)

  if mapCode[nx][ny]==0 and visited_map[nx][ny]==0:
    count+=1
    x=nx
    y=ny
    visited_map[x][y]=1
    turn_time=4
    # print(x, y)
  else :
    turn_time-=1

print(count)