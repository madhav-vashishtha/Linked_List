class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

a = DoublyNode(5)
b = DoublyNode(3)
c = DoublyNode(7)

a.next = b
b.prev = a
b.next = c
c.prev = b

head = a

print("FORWARD")

print(head.data)
print(head.next.data)
print(head.next.next.data)

print("BACKWARD")

print(c.data)
print(c.prev.data)     
print(c.prev.prev.data)

