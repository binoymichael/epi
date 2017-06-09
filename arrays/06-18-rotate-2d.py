def rotate(arr):
    n = len(arr)
    return [[arr[n - 1 - x][y] for x in range(n)] for y in range(n)]

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(arr))
arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

#TODO: Read an do variants inplace etc
