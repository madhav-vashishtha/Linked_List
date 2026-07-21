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


def reverseList(head):
    curr = head
    prev = None
    nxt = None

    while curr!=None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev 

head = take_input()

print("\nOriginal Linked List:")
printLL(head)

head = reverseList(head)

print("\nReversed Linked List:")
printLL(head)


