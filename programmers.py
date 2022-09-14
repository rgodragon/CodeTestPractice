s = [1, 2, 3, 4]
a = [-1, -2, -3, -4]
t = [-1, -1]


# def solution(s):
#     #s = list(s.split())
#     print(min(s), max(s))
#     return

# solution(s)

# def solution(s):
#     return min(s), max(s)

# solution(s)

### 내풀이
def solution(s):
    a=list(map(int, s.split()))
    a.sort()
    str = '%d %d'%(a[0], a[len(a)-1])
    return str

### 다른 사람 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
