n, k = input().split()
n = int(n)
k = int(k)
count1 = 0
count2 = 0
totalCount = 0

#print(n % k)
#print(n // k)

while (n % k != 0):
    n = n - 1
    count1 += 1

count2 = n // k

# if (n % k == 0):
# else:

totalCount = count1 + count2
print(totalCount)
