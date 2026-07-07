class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def isPalindrome(self,head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        print("List:", arr)
        print("Reverse:", arr[::-1])

        return arr == arr[::-1]
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

obj = Solution()
print("Is Palindrome?", obj.isPalindrome(head))

head = ListNode(1)
head.next = ListNode(2)

obj = Solution()
print("Is Palindrome?", obj.isPalindrome(head))

