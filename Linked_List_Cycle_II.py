class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectCycle(head):
    slow = head
    fast = head

    hasCycle = False

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            hasCycle = True
            break

    if not hasCycle:
        return None

    l = 0
    while slow.next != fast:
        slow = slow.next
        l += 1

    l += 1
    slow = slow.next

    slow = head
    fast = head

    for i in range(l):
        fast = fast.next

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

#Example 1

n1 = Node(3)
n2 = Node(2)
n3 = Node(0)
n4 = Node(-4)

n1.next = n2
n2.next = n3
n3.next = n4

n4.next = n2

head = n1

ans = detectCycle(head)

if ans == None:
    print("No Cycle")
else:
    print("Cycle starts at node =", ans.data)


#Example 2

n1 = Node(1)
n2 = Node(2)

n1.next = n2
n2.next = n1    

head = n1

ans = detectCycle(head)

if ans == None:
    print("No Cycle")
else:
    print("Cycle starts at node =", ans.data)

#Example 3

n1 = Node(1)

head = n1

ans = detectCycle(head)

if ans == None:
    print("No Cycle")
else:
    print("Cycle starts at node =", ans.data)




    