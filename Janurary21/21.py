def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ptr_to_node = node = ListNode(0)

    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1=l1.next
        else:
            node.next = l2
            l2=l2.next
        node = node.next
    node.next = l1 or l2
    return ptr_to_node.next
