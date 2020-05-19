'''
in sliding window technique we add and subtract the
last one and first one respectively which was present
next to window and first which present in the window

sliding window technique is the optimised one for
finding the maximum no in the consecutive array of
k size
the complexity for this is O(n)

'''


from time import time
start_time = time()

arr = [1, 9, -1, -1, 7, 3, -1, 2]


def brute_force(a, k):
    n = len(a)
    maxsum = 0
    for i in range(0, n-k):
        s = 0
        for j in range(i, i+k):
            s = s+a[j]
        maxsum = max(maxsum, s)
    return maxsum


def sliding_window(a, k):
    n = len(a)
    window_sum = sum(a[:k])
    sum_max = window_sum
    for i in range(k, n):
        window_sum = window_sum+a[i]-a[i-k]
        sum_max = max(sum_max, window_sum)
    return sum_max


print(brute_force(arr,4))
brutetime = (time()-start_time)*10**9
print(brutetime)
bt=time()
print(sliding_window(arr, 4))
opttime = (time()-bt)*10**9
print(opttime)