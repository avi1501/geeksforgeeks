a=[20,30,40,29,11,55,41,47,99,45,60]
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
bubblesort(a)
print(a)