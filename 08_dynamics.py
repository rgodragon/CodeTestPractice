# 피보나치 함수를 재귀함수로 구현 -> 탑다운
# def fibo(x):
#     #print(x)
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x - 1) + fibo(x - 2)

#print(fibo(5))

# 한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
# d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 -> 탑다운
# def fibo(x):
#     #print(x)
#     if x == 1 or x == 2:
#         return 1
#     #이미 계산 했는지 확인
#     if d[x] != 0:
#         return d[x]
#     #처음 계산하는거는 그대로 DP테이블에 저장
#     d[x] = fibo(x - 1) + fibo(x - 2)
#     return d[x]

# print(fibo(30))

# # 피보나치 함수를  반목문으로 구현 -> 보텀업
# d = [0] * 11
# d[1] = 1
# d[2] = 1
# n = 10

# for i in range(3, n + 1):
#     print(d)
#     d[i] = d[i - 1] + d[i - 2]

# print(d[n])

###실전문제 1로 만들기

# x = int(input())
# num = 0
# #print(247 % 5)

# while (x != 1):

#     if x % 5 == 0:
#         x = x // 5

#     elif x % 5 <= 2:
#         x = x - 1

#     else:
#         if x % 3 == 0:
#             x = x // 3
#         elif x % 2 == 0:
#             x = x // 2

#     print(x)
#     num = num + 1

# print(num)

###실전문제 1로 만들기 / 풀이
# 같은 값이 여러개 필요한 경우임
# 큰수가 작은 수들로 나누어질 수 있음
# dynamic 방식으로 풀 수 있다.
# 여러 방식(-1, /2, /3, /5)의 모든 경우를 탐색한 후에, 가장 작은 방식을 택한다.(하나씩 비교하며 min을 최종으로 선택) 다만 이미 계산된 친구들을 활용한다.
# x = int(input())
# d = [0] * 30

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1
#     print(i, d[i])
#     if i % 2 == 0:
#         print(i, d[i // 2] + 1)
#         d[i] = min(d[i], d[i // 2] + 1)  # 요소 중 가장 작은거
#     if i % 3 == 0:
#         print(i, d[i // 3] + 1)
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         print(i, d[i // 5] + 1)
#         d[i] = min(d[i], d[i // 5] + 1)
#     #print(i, d[i], d)
# print(d[x])

#https://www.youtube.com/watch?v=G3y1E564udo

# print(15 // 5)

# x = int(input())
# num = 0

# def cal(n):
#     global num
#     if n % 5 == 0:
#         n = n // 5
#     elif x % 5 <= 2:
#         n = n - 1
#     else:
#         if x % 3 == 0:
#             n = n // 3

#         elif x % 2 == 0:
#             n = n // 2
#     num += 1
#     print(n)
#     if n == 1:
#         print(num)
#     else:
#         return cal(n)

# cal(x)

# x = int(input())
# d = [0] * 30001
# d[1] = 0

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)

# print(d[x])

###############   실전문제 개미전사 / 시도 ##################

# n = int(input())
# warehouse = list(map(int, input().split()))
# food = 0
# for i in range(0, n):
#     for k in range(n - 1, i + 1, -1):
#         food = max(food, warehouse[i] + warehouse[k])
#         # print('food : ', food)
#         print('food : ', food)

# print(food)

# ###############   실전문제 개미전사 / 풀이 ##################
# #어떻게 다이나믹 프로그래밍으로 푸는 지 알 수 있는가? 이전에 한번 구해둔 답과 비교해가면서 알아낼 수 있기 때문에.
# # 내가 처음에 푼 코드에서는 이전에 구해둔 답을 계속 들고가면서 풀었음. 그걸 다이나믹한 방법으로 하는걸 몰랐을 뿐.
# n = int(input())
# warehouse = list(map(int, input().split()))
# d = [0] * 100
# d[0] = warehouse[0]  # 점화식에 쓰여있는 -만큼 초기값 주기 해주기
# d[1] = warehouse[1]

# for i in range(2, n):
#     # print(i)
#     d[i] = max(d[i - 1], d[i - 2] + warehouse[i])  # 이전 값과, 현재 쓰여진 값과 이전이전값의 비교

# print(d[n - 1])


###############   실전문제 바닥전사/ 시도 ##################
# n = int(input())
# d=[0]*1000
# d[0]=1
# d[1]=3

# for i in range(2, n):
#   d[i]=d[i-2]*2+d[i-1]

# print(d[n-1]%796796)  

###############   실전문제 화폐구성/ 시도 ##################
# n,m = map(int, input().split())
# money= [int(input()) for _ in range(n)]
# remain = m
# num = 0
# flag = 0
# # print(money)
# while remain>0:
#   num+=1
#   current_remain = remain
#   for i in range(n):
#     if current_remain-money[i]>=0:
#       remain = min(remain, current_remain-money[i])
#       flag += 1
#       if remain == 0:
#         print(num)
      
#     if flag==0:
#       print(-1)
#       remain=-1
#       break
    
#   flag = 0

# ###############   실전문제 화폐구성/ 풀이 ##################
n,m = map(int, input().split())
money= [int(input()) for _ in range(n)]
money.sort()
d=[m+1]*(m+1)
d[0]=0 # 초기값 중요!!
       
for i in range(n):
  for k in range(1, m+1):
    # if k%money[i] ==0:
    #   d[k]=min(d[k], k//money[i]) // 이것도 답이 될 수 있으나 연산속도 더 필요함.

    if k-money[i]>=0 and d[k-money[i]]!=m+1:
      d[k]=min(d[k], d[k-money[i]]+1)

# print(d)
if d[m]==m+1:
  print(-1)
else :
  print(d[m])
      
    
