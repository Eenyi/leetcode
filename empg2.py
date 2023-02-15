def sub_arr_sum(arr, start, end):
    sum = 0
    for i in range(start, end):
        sum = sum+arr[i]
    return sum

def ArrayChallenge(arr):
    if len(arr) == 0: return 0
    elif len(arr) == 1: return arr[0]
    else:
        max_sum = arr[0]
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)+1):
                if max_sum < sub_arr_sum(arr, i, j):
                    max_sum = sub_arr_sum(arr, i, j)
    return max_sum

print(ArrayChallenge([1, 2, 3, 4, 5]) == 15 )
print(ArrayChallenge( [-2, -5, -1, -3, -4]) == -1 )
print(ArrayChallenge([2, -4, 6, 8, -10, 100]) == 104 )
print(ArrayChallenge([1, 2, 1, 2, 1, 2, 1]) == 10 )
print(ArrayChallenge([5]) == 5 )
print(ArrayChallenge([100, -100, 200, -200, 300, -300]) == 300 )
print(ArrayChallenge([])==0)