a=[20,30,40,29,11,55,41,47,99,45,60]
def merge(a,b):
    c=[]
    i=j=0
    while(i<len(a) and j<len(b)):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if(i==len(a)):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c

def mergesort(a):
    if(len(a)<=1):return a
    left,right=mergesort(a[:len(a)//2]),mergesort(a[len(a)//2:])
    return merge(left,right)
  

print(mergesort(a))  

