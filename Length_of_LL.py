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

def lenthOfLL(head):
    temp = head
    ans = 0

    while(temp!=None):
        temp = temp.next
        ans = ans + 1

    return ans


headOfLL = take_input()

length = lenthOfLL(headOfLL)
print(length)



