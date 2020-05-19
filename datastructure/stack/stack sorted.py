def sortInsert(s , element): 
      
    if len(s) ==0 or element > s[-1]:
        s.append(element)
    else:
        temp = s.pop()
        sortInsert(s,element)
        s.append(temp) 
  
# Method to sort stack 
def sortStack(s): 
    if len(s) != 0:
        temp = s.pop()
        sortStack(s)
        sortInsert(s,temp)
  
# Printing contents of stack 
def printStack(s): 
    for i in s[::-1]: 
            print(i , end=" ") 
    print() 
      
# Driver Code 
if __name__=='__main__': 
    s = [ ] 
    s.append(30) 
    s.append(-5) 
    s.append(18) 
    s.append(14) 
    s.append(-3) 
  
    print("Stack elements before sorting: ") 
    printStack(s) 
  
    sortStack(s) 
  
    print("\nStack elements after sorting: ") 
    printStack(s) 
  