class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

a = Node(5)
b = Node(3)
c = Node(7)

a.next = b
b.next = c
c.next = a

head = a

curr = head

while True:
    print(curr.data,end="->")
    curr = curr.next
    if curr==head:
        break

print()


