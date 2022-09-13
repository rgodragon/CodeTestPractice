# horizon=['a','b','c','d','e','f','g','h']
# vertical=[1,2,3,4,5,6,7,8]

input = list(input())

horizon = input[0]
vertical = input[1]
possibleMaxCount = 8

# print(input[0], input[1])

directions = ['RRU', 'RRD', 'LLU', 'LLD', 'UUR', 'UUL', 'DDR', 'DDL']
unable_horizon = False
unable_vertical = False

# if(horizon == 'a')
# if(horizon == 'b')
# if(horizon == 'g')
# if(horizon == 'h')

for direction in directions:
    if (horizon == 'a' and 'L' in direction): unable_horizon = True
    if (horizon == 'b' and 'LL' in direction): unable_horizon = True
    if (horizon == 'g' and 'RR' in direction): unable_horizon = True
    if (horizon == 'h' and 'R' in direction): unable_horizon = True

    if (vertical == '1' and 'U' in direction): unable_vertical = True
    if (vertical == '2' and 'UU' in direction): unable_vertical = True
    if (vertical == '7' and 'DD' in direction): unable_vertical = True
    if (vertical == '8' and 'D' in direction): unable_vertical = True
    #print(direction, unable_horizon, unable_vertical)

    if (unable_horizon or unable_vertical): possibleMaxCount -= 1
    unable_horizon = False
    unable_vertical = False

print(possibleMaxCount)

# mysite = 'Site name is webisfree.'
# if 'webisfre' in mysite:
#     print('Okay')
