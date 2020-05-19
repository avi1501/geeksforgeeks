'''

we have given an array which is not sorted so we have to find the longest subequence of in that array
like in given example 
arr=[-1,3,4,5,2,2,2,2]

so the increasing subsequence of an array is like 
---------------
--------------->[-1,3,4,5]
--------------->[-1,2,2,2,2]
---------------
so the second one is the longest one so the answer will be 5



'''
from time import time

def longestsubsequence(arr):
    n=len(arr)
    a=[1]*n
    for i in range(n):
        for j in range(i):
            if arr[i] >= arr[j]:
                a[i]=max(a[j],a[i])+1
    print(a)
    return max(a)

def longestsubsequenc_e(arr):
    n=len(arr)
    a=[1]*n
    for i in range(n):
        for j in range(i):
            if arr[i] >= arr[j]:
                a[i]=max(a[j],a[i])+1
    print(a)
    return max(a)




arr=[-1,3,4,5,2,2,2,2]
start=time()
print(longestsubsequence(arr))
print(time()-start)
start=time()
print(longestsubsequence(arr))
print(time()-start)

