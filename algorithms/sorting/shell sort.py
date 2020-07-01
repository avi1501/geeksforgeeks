from time import time
a=[10,14,19,26,27,31,1,33,35,42,44,2]
start=time()

def insertionsort(a,n):
   for i in range(1,n):
       j = i -1
       key = a[i]
       while(j >= 0 and key < a[j]):
           a[j+1] = a[j]
           j -= 1
       a[j+1]=key


def shell_sort(a):
    n=len(a)
    k=1
    while(k<n/3):
        k=k*3+1
    k = n//2
    while(k>0):
        j=k
        while(j<n):
            i=j-k
            while(i>0):
                if(a[i+k]>=a[i]):
                    break
                else:
                    a[i+k],a[i]=a[i],a[i+k]
                    i=i-k
            j+=1
        k=k//2
    insertionsort(a,n)
    

shell_sort(a)
print(a)


passedtime=time()-start
print(passedtime)
