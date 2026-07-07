class node:
    def __init__(self,value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while temp != None:
        print(temp.data)
        temp = temp.next

    return


first = node(1)
second = node(2)
third = node(3)

first.next = second
second.next = third

first.next

head = first

print_LL(head)


