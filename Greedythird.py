# n=3
# m=4




# arr=[3,1,2]
# arr1=[4,1,4]
# arr2=[2,2,2]

# arr.sort()
# arr1.sort()
# arr2.sort()

# arrFinal = [arr[0], arr1[0], arr2[0]]

# arrFinal.sort(reverse=True)
# print (arrFinal[0])


n,m = input().split()
n=int(n)
m=int(m)
mazes = [list(map(int, input().split())) for _ in range(n)]
#mazes = [list(map(input().split())) for _ in range(n)]
#num_list = list(map(int, input().split()))
#t_d = int([list(map(int, input().split())) for _ in range(n)])

#t_d = [list(map(int, input().split())) for _ in range(n)]
#print(t_d)
 
largest = 0

for maze in mazes:
  #print(maze)
  maze.sort()
  if(maze[0]>=largest) : largest = maze[0]

print(largest)



# arr.sort(reverse=True)
# print(arr)

