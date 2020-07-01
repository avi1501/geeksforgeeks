a=[20,30,40,29,11,55,41,47,99,45,60,33]

'''
i can't able to solve this problem recursively 
this code needs to be updated as there is several problems in this

'''
def merge(a,low,mid,ub):
    i = a[low:mid]
    k = a[mid:ub]
    p = q = 0
    z = low
    while(p < len(i) and q < len(k)):
        print(i,"ad",k)
        if i[p] <= k[q]:
            a[z] = i[p]
            p += 1
            z += 1
        else:
            a[z] = k[q]
            q += 1
            z += 1
    if(p < mid):
        for t in i:
            a[z] = i
            z += 1
    elif(q < ub):
        for t in k:
            a[z] = t
            z += 1

def mergesort(a, low, hi):
    if(low<hi):
        mid = (low+hi)//2
        mergesort(a, low, mid)
        mergesort(a, mid+1, hi)
        merge(a, low, mid, hi)
hi=len(a)-1
mergesort(a,0,hi)
print(a)
