class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data,end="->")
        temp = temp.next

    print()
    return

def take_input():
    value = int(input("Enter the value of Node :- "))
    head = None
    
    while(value != -1):
        newNode = Node(value)
        if(head == None):
            head = newNode
        else:
            temp = head
            while(temp.next!=None):
                temp=temp.next
            
            temp.next = newNode
        
        value = int(input("Enter the value of Node :- "))
    
    return head

def insert_at_head(head,data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head


def insert_at_index(head,data,index):
    if(index ==0):
        return insert_at_head(head,data)
    
    newNode = Node(data)
    temp = head
    count = 0

    while temp is not None and count < index - 1:
        temp = temp.next
        count+=1

    if(temp is None):
        print("Index out of bounds, please check index")
        return head
    
    newNode.next = temp.next
    temp.next = newNode
    return head

head = take_input()

head = insert_at_index(head,45,4)
print("After Inserting at Tail")
print_LL(head)
