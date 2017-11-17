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

    def __init__(self, str=None):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
        if str != None:
            for i in str.split():
                self.add_last(i)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise Empty
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise Empty
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
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    fnlist = DoublyLinkedList()
    return merge_sublists(srt_lnk_lst1, srt_lnk_lst2, fnlist)


def merge_sublists(lnk1, lnk2, fnlist):
    if lnk1.is_empty() and lnk2.is_empty():
        return fnlist
    elif lnk1.is_empty():
        temp = lnk2.delete(lnk2.first_node())
        fnlist.add_last(temp)
        return merge_sublists(lnk1, lnk2, fnlist)
    elif lnk2.is_empty():
        temp = lnk1.delete(lnk1.first_node())
        fnlist.add_last(temp)
        return merge_sublists(lnk1, lnk2, fnlist)
    else:
        temp1 = lnk1.first_node().data
        temp2 = lnk2.first_node().data
        if temp1 < temp2:
            temp = lnk1.delete(lnk1.first_node())
            fnlist.add_last(temp)
            return merge_sublists(lnk1, lnk2, fnlist)
        else:
            temp = lnk2.delete(lnk2.first_node())
            fnlist.add_last(temp)
            return merge_sublists(lnk1, lnk2, fnlist)