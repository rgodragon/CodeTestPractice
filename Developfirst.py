N = int(input())
routes = input().split()

#print(routes)

X = 1
Y = 1

for route in routes:
    if (route == 'D' and X != N): X += 1
    if (route == 'U' and X != 1): X -= 1
    if (route == 'R' and Y != N): Y += 1
    if (route == 'L' and Y != 1): Y -= 1

print(X, Y)
