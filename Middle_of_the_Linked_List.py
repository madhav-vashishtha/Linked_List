class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

# METHOD:-1

def middleNode(head):
    
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow


head = take_input()

middle = middleNode(head)

print("Middle Node =", middle.data)

# METHOD:-2

def middle_Node(head):
    curr = head 

    l = 0
    while curr!=None:
        curr = curr.next
        l+=1

    curr = head
    for i in range(l//2):
        curr = curr.next

    return curr

head = take_input()

middle = middle_Node(head)

print("Middle Node =", middle.data)

