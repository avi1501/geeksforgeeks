'''
this is a linear method of searching 
in this we simply iterate over a loop
time complexity for this is
best case  -  O(1)
avg/best case - O(n)

'''

a=[1,5,3,6,4,9,8]
x=6
n=len(a)
s='not found'
for i in range(n):
    if(a[i]==x):
        s=i
        break
print(s)

