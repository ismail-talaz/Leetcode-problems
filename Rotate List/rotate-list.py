class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return head

        length,tail=1,head
        while (tail.next):
            length+=1
            tail=tail.next
        k=(k%length)
        if k==0:return head
        
        newTail=head
        for _ in range(length-k-1):
            newTail=newTail.next
        tail.next=head
        head=newTail.next
        newTail.next=None
        return head
