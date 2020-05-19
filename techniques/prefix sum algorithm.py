'''
prefix sum algorithm is used when we have to find
the sum of consecutive elements in array for multiple
times
By using prefix sum algorithm we can find the sum
with the complexity of O(1)

if we not use prefix sum algorithm  then we have to
run it n times which make its complexity to O(n)

so prefix sum algorithm is efficient here

'''




from time import time
arr = [1, 9, -1, -1, 7, 3, -1, 2]*10**3


def prefix_sum_algo(x):
    n = len(x)
    for i in range(n-1):
        x[i+1] = x[i]+x[i+1]


def findsum(a, i, j):
    return a[j]-a[i-1]


def findsum1(a, i, j):
    return sum(a[i:j+1])


start_time = time()
prefix_sum_algo(arr)
print(arr)
print(findsum(arr, 1, 500))
end_time = time()-start_time
print(end_time)
arr = [1, 9, -1, -1, 7, 3, -1, 2]*10**3
start_time = time()
print(findsum1(arr, 1, 500))
end_time = time()-start_time
print(end_time*10**9)