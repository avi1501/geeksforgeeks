a=[10,14,19,26,27,31,33,35,42,44]
a.sort()
def interpolation_search(a,x):
    lo=0
    n=len(a)
    hi=n-1
    while(lo<=hi):
        mid=int(lo+((hi-lo)/(a[hi]-a[lo]))*(x-a[lo]))
        if(a[mid]==x):
            return mid
        elif(a[mid]<x):
            lo=mid+1
        else:
            hi=mid-1
    return 'not found'

print(interpolation_search(a,99))
