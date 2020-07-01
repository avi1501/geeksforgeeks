from time import time
a=[10,14,19,26,27,31,1,33,35,42,44,2]
start=time()

def insertionsort(a,n):
    for i in range(1,n):
        j=i-1
        key=a[i]
        while(a[j]>key and j>=0):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key

def shell_sort(a):
    n = len(a)
    k = n//2
    j = n
    while(k>0):
        j = 0
        while(j<n-k):
            i = j
            while(i>0):
                if a[i] > a[i+k]:
                    a[i],a[i+k] = a[i+k],a[i]
                    i = i - k 
                else:
                    break
                        
            j = j+1 
        k = k //2  
    insertionsort(a,n) 

shell_sort(a)
print(a)


passedtime=time()-start
print(passedtime)
