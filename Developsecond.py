#첫 시도
N = int(input())

second1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
second10 = [0, 1, 2, 3, 4, 5]

minute1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
minute10 = [0, 1, 2, 3, 4, 5]

hours = list(range(N + 1))

count = 0
#print(hours)

# for h in hours:
#     for mm in minute10:
#         for m in minute1:
#             for ss in second10:
#                 for s in second1:
#                     if (h == 3 or mm == 3 or m == 3 or ss == 3 or s == 3):
#                         count += 1
#                     #print(i, j)

# print(count)

# 완전 탐색은 100만개 이하

for h in hours:
    for m in range(60):
        for s in range(60):
            # print(str(h) + str(m) + str(s))
            if '3' in (str(h) + str(m) + str(s)): count += 1

print(count)
