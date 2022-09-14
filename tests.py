### 스택과 큐
# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue)

### 재귀 함수
# def recursive_function(i):
#     if i == 100: #종료 조건 꼭 넣어줘야함
#         return
#     print(i, '번쨰 재귀함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
#     recursive_function(i + 1)
#     print(i, '번째 재귀함수를 종료합니다.')

# recursive_function(1)


### 재귀 함수
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print('반복적으로 구현:', factorial_iterative(5))


def factorial_reculsive(n):
    if n <= 1:
        return 1
    return n * factorial_iterative(n - 1)


print('반복적으로 구현:', factorial_reculsive(5))


def uclid(a, b):
    if a % b == 0:
        #print(b)
        return b
    else:
        return uclid(b, a % b)


print(uclid(192, 162))
