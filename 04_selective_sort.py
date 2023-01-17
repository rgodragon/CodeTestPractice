###선택 정렬
# 가장 왼쪽 원소부터 남은 원소들끼리 대소 비교
# 대소 비교중 더 작은 원소를 가장 작은 원소로 지정
# 가장 작은 원소와 (비교대상인) 가장 왼쪽 원소 자리 바꾸기

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         print(array[min_index], array[j], min_index)
#         if array[min_index] > array[j]:
#             min_index = j

#     array[i], array[min_index] = array[min_index], array[i]  # 스와프

# print(array)

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]

# print(array)

### 삽입 정렬
# (비교대상)가장 왼쪽 원소부터 오른쪽 원소와 대소 비교
# 비교대상인 왼쪽 원소보다 오른쪽 원소가 작으면 왼쪽 원소 옆으로 이동
# 한번 더 왼쪽 원소보다 오른쪽 원소가 작으면, 앞서 왼쪽에 있는 원소들과 대소 비교하여 어디에 들어갈지 판단. 맨 왼쪽 부터 비교해서 크면 오른쪽 작으면 왼쪽
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# #print(array)

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         #j는 현재 인덱스부터 왼쪽에 있는 것들 하나씩 체크함. 이미 옮겨진 데이터도 또 옮겨져야함.
#         if array[j] < array[j - 1]:
#             #print(array[j], array[j - 1])
#             array[j], array[j - 1] = array[j - 1], array[j]
#             print(array)
#         else:
#             break
# #print(array)

### 퀵 정렬
# 리스트 첫번째 원소가 피벗
# 피벗으로 부터 오른쪽으로 가며 피벗 보다 작은 거 찾기
# 리스트 마지막 원소부터 왼쪽으로 가며 피벗 보다 큰 거 찾기
# 둘 다 찾아지면 서로 자리 바꾸기
# 피벗보다 큰 원소와 작은 원소의 위치가 엇갈리면, 작은 원소와 피벗 원소를 자리 바꾸면 분할 완료.

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):  # start는 시작점 0, end는 리스트 크기 -1
#     if start >= end:  # 원소가 한개인 경우 종료.
#         print('shit', array, start, end)
#         return
#     pivot = start
#     left = start + 1  #리스트 순서
#     right = end  #리스트 순서
#     print('start', array, start, end, left, right)

#     #왼쪽 원소가 오른쪽보다 크지 않을 때까지만 반복s
#     while (left <= right):
#         #피벗보다 큰 데이터 찾을 때까지 반복
#         while (left <= end and array[left] <= array[pivot]):
#             left += 1
#         #피벗보다 작은 데이터 찾을 때까지 반복
#         while (right > start and array[right] >= array[pivot]):
#             right -= 1
#         # 엇갈렸다면 작은 데이터와 피벗을 교체
#         if (left > right):
#             array[right], array[pivot] = array[pivot], array[right]
#         # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#         else:
#             array[left], array[right] = array[right], array[left]
#         print('result', array, start, end, left, right)

#     #분할 이후 왼쪽 부분과 오른쪽 부분에 대해서 각각 정렬 수행
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)

# quick_sort(array, 0, len(array) - 1)
# print(array)

### 계수 정렬
# 양의 정수만 가능
# 가장 작은 데이터(min)부터 큰 데이터가(max) 담기는 리스트 구성
# 리스트 인덱스에 일치하는 값에 count를 올리기
# 카운트 만큼 출력하기
# 모든 원소 값이 0보다 크다고 가정
# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# # 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화). 0,9까지니까 10개 반복
# count = [0] * (max(array) + 1)
# print(count)
# print(len(array))

# for i in range(len(array)):
#     count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가
#     print(count)

# for i in range(len(count)):  #리스트에 기록된 정렬 정보 확인
#     for j in range(count[i]):
#         print(i, end=' ')  # 띄어쓰기를 구분으로 등장한 횟수 만큼 인덱스 출력

### 실전문제 1
# 기본 정렬 라이브러리
# n = int(input())
# array = []

# for i in range(n):
#     array.append(int(input()))

# array.sort(reverse=True)
# for i in range(len(array)):
#     print(array[i], end=' ')

#계수 정렬
# n = int(input())
# array = []

# for i in range(n):
#     array.append(int(input()))

# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count) - 1, -1, -1):
#     for j in range(count[i]):
#         print(i, end=' ')

#print(array)

### 실전문제 2
# n = int(input())
# scores = {}

# for i in range(n):
#     input_data = input().split()
#     scores[input_data[0]] = int(input_data[1])
# scores = sorted(scores.items(), key=lambda item: item[1])

# for i in range(len(scores)):
#     print(scores[i][0])

##lambda 매개변수 : 표현식
# lambfa 인공지능 분야나 AutoCAD 설계 프로그램에서 쓴이는 Lisp언어
# https://wikidocs.net/64

# def haf(a, b):
#     return a + b
# print(haf(2, 3))
# print((lambda x, y: x + y)(2, 3))
# test_list = list(map((lambda x: x**2),
#                      [0, 1, 2, 3, 4]))  #[0,1,2,3,4] 리스트를 받아서 제곱함
# print(test_list)

### 실전문제 3
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#print(a)
a.sort()
b.sort(reverse=True)

#print(a, b)

for i in range(k):
    if b[i] > a[i]:
        a[i], b[i] = b[i], a[i]
    else:
      break
    #print(a, b)

print(sum(a))
