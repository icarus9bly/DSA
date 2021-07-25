# LRU Cache with Double linked list
class LinkedListNode(object):
    def __init__(self, key=None, val=-1):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def appendHead(self, node):
        node.next, node.pre = self.head, None
        if self.head:
            self.head.pre = node
        self.head = node

        if not self.tail:
            self.tail = self.head

        self.size += 1

    def remove(self, node):
        if not node:
            return

        pre, next = node.pre, node.next
        if pre:
            pre.next = next
        if next:
            next.pre = pre

        if self.head == node:
            self.head = next

        if self.tail == node:
            self.tail = pre

        self.size -= 1
        return node

    def removeTail(self):
        return self.remove(self.tail)

    def advance(self, node):
        self.remove(node)
        self.appendHead(node)


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.record = {}
        self.linkedList = LinkedList()

    def get(self, key):
        if key not in self.record:
            return -1

        self.linkedList.advance(self.record[key])
        return self.record[key].val

    def put(self, key, value):
        if key not in self.record:
            node = LinkedListNode(key, value)

            self.linkedList.appendHead(node)
            self.record[key] = node

            if self.linkedList.size > self.capacity:
                del self.record[self.linkedList.removeTail().key]
        else:
            self.record[key].val = value
            self.linkedList.advance(self.record[key])
