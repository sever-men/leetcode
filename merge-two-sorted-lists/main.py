from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return

        if list1 is None:
            return ListNode(val=list2.val, next=list2.next)

        if list2 is None:
            return ListNode(val=list1.val, next=list1.next)

        beginning = node = ListNode()

        while True:
            if list1.val >= list2.val:
                node.val = list2.val
                if list2.next is None:
                    node.next = list1
                    return beginning

                list2 = list2.next
            else:
                node.val = list1.val

                if list1.next is None:
                    node.next = list2
                    return beginning

                list1 = list1.next

            node.next = ListNode()
            node = node.next

        return result

