class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tmpHead = ListNode()
        resList = tmpHead
        
        while list1 and list2:
            if list1.val <= list2.val:
                tmpHead.next = list1
                list1 = list1.next
            
            else:
                tmpHead.next = list2
                list2 = list2.next
                
            tmpHead = tmpHead.next
            
        if list1:
            tmpHead.next = list1
            
        if list2:
            tmpHead.next = list2
            
        return resList.next