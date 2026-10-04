Class LinkedList:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
head=ListNod
        
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
        return dummy.next
head=LinkedList(1)
head.next=LinkedList(2)
head.next.next=LinkedList(3)
head.next.next.next=LinkedList(4)
head.next.next.next.next=LinkedList(5)

obj=Solution()
print(obj.generate(head,2))