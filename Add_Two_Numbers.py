class ListNode:
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
        newNode = ListNode(value)

        if head == None:
            head = newNode

        else:
            temp = head

            while temp.next != None:
                temp = temp.next

            temp.next = newNode

        value = int(input("Enter the value of Node :- "))

    return head


def addTwoNumbers(head1, head2):
        curr1 = head1
        curr2 = head2

        ans = ListNode(-1)
        c = 0 
        curr3 = ans

        while curr1!=None or curr2!=None:
            total = c
            c = 0
            if curr1!=None:
                total+=curr1.data
                curr1=curr1.next
            if curr2!=None:
                total+=curr2.data
                curr2=curr2.next

            if total>9:
                c = 1
                total-=10

            newNode = ListNode(total)
            curr3.next = newNode
            curr3 = curr3.next

        if c>0:
            newNode = ListNode(c)
            curr3.next = newNode

        return ans.next 

print("Enter First Linked List")
head1 = take_input()

print("\nEnter Second Linked List")
head2 = take_input()

print("\nFirst Linked List")
printLL(head1)

print("\nSecond Linked List")
printLL(head2)

result = addTwoNumbers(head1, head2)

print("\nAnswer Linked List")
printLL(result)
