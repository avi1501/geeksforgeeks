def bal(start,close,n,arr=[]):
    if(close==n):
        print(arr)
        return
    else:
        if(close<start):
            arr.append(')')
            bal(start,close+1,n,arr)
            arr.pop()
        if(start<n):
            arr.append('(')
            bal(start+1,close,n,arr)
            arr.pop()
bal(0,0,3)
