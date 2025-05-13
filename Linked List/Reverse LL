def reverse(head):
    prev, next = None, None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev
    return head
