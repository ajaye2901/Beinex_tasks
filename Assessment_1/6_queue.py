def enqueue(l):
    n=int(input("How many element you want to add : "))

    for i in range(n):
        k=int(input("Enter the item "))
        l.append(k)
    return l

def dequeue(l) :

    l.pop(0)
    return l 



l=[]

while True :

    option = int(input("Choose the Option"                   
                       "\n1.Enqueue(Adding element to the queue)"
                       "\n2.Dequeue(Removing the element from the queue)"
                       "\n3.Exit"
                       "\n : "))
    

    if option == 1:
        print(enqueue(l))
    
    elif option == 2:
        print(dequeue(l))
    
    elif option == 3:
        break
    else:
        print("Choose correct option")


