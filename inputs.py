import time
startTime = time.time()
### 파이썬 인풋.split
# a, b = input().split()
# print(a, b)

### 파이썬 인풋 - map함수
# a, b = map(int, input().split())
# print(a, b)

# a = ['1', '2', '3', '4']
# a = list(map(int, a))
# print(a)

# a = [1, 2, 3, 4]

# def plus(n):
#     return n + 10

#print(list(map(plus, a)))

### 파이썬 인풋 - for _ in range[n] 리스트 행렬 입력, n은 행 개수
#mazes = [list(map(int, input().split())) for _ in range(n)]


### 파이썬 리스트 컴프리핸션
# numbers = []
# for i in range(10):
#   numbers.append(i)

# print(numbers)

# numbers = [i for i in range(10) if i%2==0]
# print(numbers)

food = [(x,y) for x in ['쌈밥','치킨','피자'] for y in ['사과','아이스크림','커피']]
print(food)

# for x in ['쌈밥','치킨','피자']:
#   for y in ['사과','아이스크림','커피']:
#     print(x,y)

endTime = time.time()
print('time :', endTime-startTime)
