Class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
Class Solution:
    def generate(self,head,n):
        dummy=LinkedList(0,head)
        slow=dummy
        fast=head
        for i in range(n):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        print(dummy.next)
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

obj=Solution()
head=obj.generate(head,2)