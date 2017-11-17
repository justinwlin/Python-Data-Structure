class EmptyCollection(Exception):
    pass


class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if(self.is_empty()):
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)

class LinkedStack:
#The last of the LinkedStack is the top of the stack
    def __init__(self):
        self.dll = DoublyLinkedList()

    def push(self, e):
        self.dll.add_last(e)

    def pop(self):
        if self.dll.is_empty():
            raise("Nothing is in the stack")
        temp = self.dll.trailer.prev.data
        self.dll.trailer.disconnect()
        return temp

    def top(self):
        if self.dll.is_empty():
            raise("Nothing is in the stack")
        return self.dll.trailer.prev.data

    def is_empty(self):
        return self.dll.is_empty()

    def __len__(self):
        return self.dll.size

class LeakyStack:
#The last of the LinkedStack is the top of the stack
    def __init__(self, elem):
        self.dll = DoublyLinkedList()
        self.cap = elem

    def push(self, e):
        self.dll.add_last(e)
        if self.dll.size > self.cap:
            self.dll.header.next.disconnect()

    def pop(self):
        temp = self.dll.trailer.prev.data
        self.dll.trailer.prev.disconnect()
        return temp

    def top(self):
        return self.dll.trailer.prev.data

    def is_empty(self):
        return self.dll.is_empty()

    def __len__(self):
        return self.dll.size

def reverseDLL(x):
    firstNode = x.header.next
    secondNode = x.trailer.prev
    for i in range(1, x.size // 2 + 1):
        tempFirstNode = firstNode.data
        tempSecondNode = secondNode.data

        firstNode.data = tempSecondNode
        secondNode.data = tempFirstNode

        firstNode = firstNode.next
        secondNode = secondNode.prev
    return x


dll = DoublyLinkedList()
dll.add_first(5)
dll.add_first(4)
dll.add_first(3)
dll.add_first(2)
dll.add_first(1)

print(dll)

print(reverseDLL(dll))



