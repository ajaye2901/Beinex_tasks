def stack_push(l) :
    n=int(input("How many items you need to push into stack : "))

    for i in range(n):
        k=int(input("Enter the item : "))
        l.append(k)

    return l

def stack_pop(l):
    
    if len(l) == 0:
        print("Stack is Empty")
    else:
        l.pop()
        return l 

l=[1,2,3]

while True:
    

    option = int(input("Choose the Option"                   
                       "\n1.Push(Adding element to the queue)"
                       "\n2.Pop(Removing the element from the queue)"
                       "\n3.Exit"
                       "\n : "))

    if option == 1:
        print(stack_push(l))
    elif option == 2:
        print(stack_pop(l))
    else:
        print("Exit")
        break

