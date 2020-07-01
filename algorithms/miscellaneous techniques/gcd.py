a=int(input())
b=int(input())
def Greatest_common_divisior(a,b):
    if(b==0):
        return a
    return Greatest_common_divisior(b,a%b)

print(Greatest_common_divisior(a,b))