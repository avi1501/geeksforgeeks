def createstack():
    stack = []
    return stack
def isEmpty(stack):
    if len(stack) == 0:
        return True
    return False

def push(stack,item):
    stack.append(item)
    print(item,'pushed to stack')

def pop(stack):
    if isEmpty(stack):
        return 
    return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return
    return stack[-1]

stack = createstack()

push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(str(pop(stack))+' poped from stack')


    