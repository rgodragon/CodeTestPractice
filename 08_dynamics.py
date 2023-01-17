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

#https://velog.io/@alexms0316/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Chp-8.-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0

print(5 % 5)
