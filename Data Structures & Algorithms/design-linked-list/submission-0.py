class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0) # Dummy Node to the left
        self.right = ListNode(0) # Dummy Node to the right
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        next = self.left.next
        prev = self.left

        prev.next = newNode
        next.prev = newNode

        newNode.next = next
        newNode.prev = prev

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        next = self.right
        prev = self.right.prev
        
        prev.next = newNode
        next.prev = newNode

        newNode.next = next
        newNode.prev = prev
        
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            newNode = ListNode(val)
            next = cur
            prev = cur.prev

            prev.next = newNode
            next.prev = newNode

            newNode.next = next
            newNode.prev = prev
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            next = cur.next
            prev = cur.prev

            next.prev = prev
            prev.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)