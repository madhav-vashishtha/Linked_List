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


def hasCycle(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head = take_input()

last = head
while last.next != None:
    last = last.next

second = head.next

last.next = second

print(hasCycle(head))