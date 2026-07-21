class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    temp = head

    while temp != None:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


def take_input():
    value = int(input("Enter the value of Node :- "))
    head = None

    while value != -1:
        newNode = Node(value)

        if head == None:
            head = newNode

        else:
            temp = head

            while temp.next != None:
                temp = temp.next

            temp.next = newNode

        value = int(input("Enter the value of Node :- "))

    return head

def deleteDuplicates(head):
        # corner case
        if head==None or head.next==None:
            return head

        curr = head
        while curr!=None and curr.next!=None:
            # Duplicate
            if curr.next.data == curr.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
        
head = take_input()

print("\nOriginal Linked List:")
printLL(head)

head = deleteDuplicates(head)

print("\nRemove Dumplicates Linked List:")
printLL(head)

