m = int(input())
guests = list(map(int, input().split()))
guests.sort()

totalTime = 0
n = 0
for i in range(m, 0, -1):
    totalTime += guests[n] * i
    n += 1
print(totalTime)