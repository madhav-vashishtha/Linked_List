class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_LL(head):
    curr = head
    while curr != None:
        print(curr.data,end="->")
        curr = curr.next

    print()
    return

def take_input():
    value = int(input("Enter the value of node: "))
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

        value = int(input("Enter the value of Node: "))

    return head

head = take_input()

curr = head
while curr.next.next != None:
    curr = curr.next

curr.next = None
print("After Deletion")
print_LL(head)


