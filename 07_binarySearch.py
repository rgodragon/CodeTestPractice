###이진탐색
# 데이터를 반으로 줄여가며 탐색.
# 시간 복잡도는 O(logN)
# 출제 빈도가 높으므로 알고리즘 자체를 외워두기

# 이진 탐색 소스코드 구현(재귀 함수)
# def bianary_search(array, target, start, end):
# if start > end:
#     return None
# #중간 인덱스 찾기
# mid = (start + end) // 2
# if array[mid] == target:
#     return mid
# #중간점이 타겟보다 크면 왼쪽을, 작으면 오른쪽을 다시 탐색
# elif array[mid] > target:
#     return bianary_search(array, target, start, mid - 1)
# else:
#     return bianary_search(array, target, mid + 1, end)

# 반복문
# def bianary_search(array, target, start, end):
#     while (start <= end):
#         mid = (start + end) // 2
#         #중간 인덱스 찾기
#         if array[mid] == target:
#             return mid
#         #중간점이 타겟보다 크면 왼쪽을, 작으면 오른쪽을 다시 탐색
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = bianary_search(array, target, 0, n - 1)

# if result == None:
#     print('찾는 원소가 존재하지 않습니다')
# else:
#     print(result + 1)

# 인덱스를 쓰면 안되나요?
# print(array.index(7) + 1)

###실전문제 부품찾기

# n = int(input())
# #inboxs = list(map(int, input().split()))
# inboxs = set(map(int, input().split()))
# #set을 써야하는 이유? 리스트보다 시간 복잡도가 낮음. 딕셔너리와 동일. for i in 쓸때 참고
# # https://twpower.github.io/120-python-in-operator-time-complexity
# m = int(input())
# parts = list(map(int, input().split()))

# #print(n, inbox, m, parts)

# for part in parts:
#     if part in inboxs:
#         print('yes', end=' ')  # 띄어쓰기 끝나게
#     else:
#         print('no', end=' ')

###실전문제 떡볶이 떡 만들기

n, m = map(int, input().split())
cakes = list(map(int, input().split()))

h = (sum(cakes) - m) // n
cakes.sort(reverse=True)
#add = 0
cakes = list(map(lambda x: x - h, cakes))
#print(cakes)

if (sum(cakes) > m):
    while (sum(cakes) >= m):
        # middle = len(cakes)//2

        # if cakes[middle] > 0: #(오른 쪽값)
        #   start_end
        # elif cakes[middle] <=0 : #(왼쪽값)
        # print(cakes)
        # length = len(cakes)
        # print(length)
        count = 0

        for i in range(len(cakes)):
            #print(i)
            if cakes[i] <= 0:
                count += 1
        del cakes[len(cakes) - count:len(cakes)]

        print(cakes, h)

        if sum(cakes) == m:
            print(h)
            break
        elif sum(cakes) > m:
            h += 1
        cakes = list(map(lambda x: x - 1, cakes))
        # print(cakes, sum(cakes), m, h)

elif sum(cakes) == m:
    print(h)

n, m = map(int, input().split())
cakes = list(map(int, input().split()))
start = 0
end = max(cakes)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in cakes:
        if i > mid:
            sum += i - mid

    if sum == m:
        break
    elif sum > m:
        start = mid + 1
    else:
        end = mid - 1
print(mid)
# cakes = list(map(lambda x: x - h, cakes))

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if cakes[mid] == target:
#             return mid
#         elif cakes[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
