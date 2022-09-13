# 첫 시도
arr = [2, 4, 5, 4, 6]
m = 8
k = 3


def second_largest_number(arr, k):
    unique_nums = set(arr)
    sorted_nums = sorted(unique_nums, reverse=True)
    return sorted_nums[k]


largestNum = second_largest_number(arr, 0)
secondNum = second_largest_number(arr, 1)

result = largestNum * k * (m // k) + secondNum * (m % k)
print(result)

# 두번쨰 시도

arr.sort(reverse=True)
#print(arr[1])

largestNum = arr[0]
secondNum = arr[1]

result = largestNum * k * (m // k) + secondNum * (m % k)
print(result)
