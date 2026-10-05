class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
class Solution:
    def generate(self,head,n):
        dummy=ListNode(0,head)
        slow=dummy
        fast=head
        for i in range(n):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

obj=Solution()
head=obj.generate(head,2)

current=head
while current:
    print(current.val, end=" ")
    current=current.next