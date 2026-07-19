class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    
    p1 = head
    p2 = head

    for i in range(n):
        p2 = p2.next

    if p2 == None:
        head = head.next
        return head

    while p2.next != None:
        p2 = p2.next
        p1 = p1.next

    p1.next = p1.next.next

    return head
    
# Linked List Print Function
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("EXAMPLE:1")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Before:")
printList(head)

head = removeNthFromEnd(head, 2)

print("After:")
printList(head)

print("EXAMPLE:2")

head = ListNode(1)

print("Before:")
printList(head)

head = removeNthFromEnd(head, 1)

print("After:")
printList(head)

print("EXAMPLE:3")

head = ListNode(1)
head.next = ListNode(2)

print("Before:")
printList(head)

head = removeNthFromEnd(head, 1)

print("After:")
printList(head)
