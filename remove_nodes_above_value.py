
class LinkedListNode(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, head):
        self.head = head

    def remove_nodes_above_value(self, value):
        """Remove nodes greater than value.

        Example:

        
        
        
        >>> three = LinkedListNode(3, four)
        >>> two = LinkedListNode(2, three)
        >>> one = LinkedListNode(1, two)
        >>> head = LinkedListNode(0, one)

        """
        current = self.head

        while current.next is not None:
            if current.next > value:
                current.next = current.next.next
            if current.next.next is None and current.next > value:
                current.next = None
            current = current.next
