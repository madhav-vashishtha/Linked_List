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


def getIntersectionNode(headA, headB):

    p1 = headA
    p2 = headB

    c = 0

    while True:

        if p1 == p2:
            return p1

        p1 = p1.next
        p2 = p2.next

        if p2 == None:
            c += 1
            p2 = headA

        if p1 == None:
            p1 = headB

        if c > 1:
            return None



common = Node(8)
common.next = Node(4)
common.next.next = Node(5)



headA = Node(4)
headA.next = Node(1)
headA.next.next = common


headB = Node(5)
headB.next = Node(6)
headB.next.next = Node(1)
headB.next.next.next = common


print("Linked List A:")
printLL(headA)

print("Linked List B:")
printLL(headB)

ans = getIntersectionNode(headA, headB)

if ans != None:
    print("Intersection Node =", ans.data)
else:
    print("No Intersection")

