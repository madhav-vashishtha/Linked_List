class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while temp!=None:
        print(temp.data,end="->")
        temp = temp.next

    print()
    return

def take_input():
    value = int(input("Enter the value of Node: "))
    head = None

    while value != -1:
        newNode = Node(value)
        if head == None:
            head = newNode
        else:
            temp = head
            while temp.next!=None:
                temp=temp.next

            temp.next = newNode

        value = int(input("Enter the value of Node: "))

    return head

def insert_at_tail(head,data):
    newNode = Node(data)
    if(head is None):
        return newNode
    
    temp = head
    while(temp.next != None):
        temp = temp.next

    temp.next = newNode

    return head


def insert_at_tail_recursively(head,data):
    if(head is None): # base
      newNode = Node(data)
      return newNode
      
    head.next = insert_at_tail_recursively(head.next,data)

    return head

head = take_input()

head = insert_at_tail_recursively(head,45)
print("After Inserting at Tail")
print_LL(head)


def insert_at_index_recursively(head,data,index):
    if(index ==0):
        return insert_at_tail(head,data)
    if(head == None):
        print("Index is out of bounds")
        return head
    
    head.next = insert_at_index_recursively(head.next,data,index-1)

    return head

head = take_input()

head = insert_at_index_recursively(head,45,3)
print("After Inserting at Index")
print_LL(head)
