def fabonicci_no_recursive_approach(no):
    a=0
    b=1
    if(no==0):
        return a
    elif no==1:
        return b
    else:
        return fabonicci_no_recursive_approach(no-1)+fabonicci_no_recursive_approach(no-2)


def fabonicci_series_iterative_approach(no):
    a=0
    b=1
    if(no==0):
        print(a)
    elif(no==1):
        print(a,b)
    else:
        print("{} \n{}".format(a,b))
        while(no-2>=0):
            temp=a+b
            a=b
            b=temp
            print(temp)
            no = no-1


fabonicci_series_iterative_approach(10)
no=0
while(no<15):
    print(fabonicci_no_recursive_approach(9))
    no += 1
