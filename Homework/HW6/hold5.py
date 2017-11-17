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


    def __init__(self, str = None):
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

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    #final_llst = DoublyLinkedList()
    curr1 = srt_lnk_lst1.header.next
    curr2  = srt_lnk_lst2.header.next
    final = DoublyLinkedList()
    return merge_sublists(final, srt_lnk_lst1, srt_lnk_lst2, curr1, curr2)

def merge_sublists(fllst, lnk1, lnk2, curr1, curr2):
    temp1 = curr1.data
    temp2 = curr2.data

    if curr1 == lnk1.trailer:
        while curr2.data != None:
            fllst.add_last(temp2)
            curr2 = curr2.next
            temp2 = curr2.data
        return fllst
    elif curr2 == lnk2.trailer:
        while curr1.data != None:
            fllst.add_last(temp1)
            curr1 = curr1.next
        return fllst
    elif int(temp1) < int(temp2):
        fllst.add_last(temp1)
        curr1 = curr1.next
        merge_sublists(fllst, lnk1, lnk2, curr1, curr2)
    elif int(temp1) > int(temp2):
        fllst.add_last(temp2)
        curr2 = curr2.next
        merge_sublists(fllst, lnk1, lnk2, curr1, curr2)
    elif int(temp1) == int(temp2):
        fllst.add_last(temp1)
        curr1 = curr1.next
        fllst.add_last(temp2)
        curr2 = curr2.next
        merge_sublists(fllst, lnk1, lnk2, curr1, curr2)
    return fllst
    # stringV = str(fllst)
    # if curr1.next == lnk1.trailer:
    #     while(curr2.data != None):
    #         fllst.add_last(curr2.data)
    #         curr2.next
    # if curr2.next == lnk2.trailer:
    #     while (curr1.data != None):
    #         fllst.add_last(curr1.data)
    #         curr1.next
    #
    # if temp1 < temp2:
    #     fllst.add_last(curr1)
    #     curr1 = curr1.next
    #     print(fllst)
    #     merge_sublists(fllst, lnk1, lnk2, curr1, curr2)
    # elif temp1 > temp2:
    #     fllst.add_last(curr2.data)
    #     curr2 = curr2.next
    #     print(fllst)
    #     merge_sublists(fllst, lnk1, lnk2, curr1, curr2)
    # elif temp1 == temp2:
    #     fllst.add_last(curr1.data)
    #     curr1 = curr1.next
    #     fllst.add_last(curr2.data)
    #     curr2 = curr2.next
    #     print(fllst)
    #     merge_sublists(fllst, lnk1, lnk2, curr1, curr2)
    #
    # return fllst

a = DoublyLinkedList("3")

b = DoublyLinkedList("")

print(merge_linked_lists(a, b))