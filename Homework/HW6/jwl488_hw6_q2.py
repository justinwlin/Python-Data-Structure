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


class Integer:
    def __init__(self, num_str):
        self.integ = DoublyLinkedList()
        for i in num_str:
            self.integ.add_last(int(i))

    def __add__(self, other):
        #OBJECT VARIABLES
        #ASSUME THAT CURSOR1 is > Cursor2

        # curr1 = self.integ.last_node()
        # curr2 = other.integ.last_node()
        #
        # final = Integer("0")
        curr1 = self.integ.last_node()
        curr2 = other.integ.last_node()
        final = Integer("0")

        if len(self.integ) < len(other.integ):
            curr1, curr2 = curr2, curr1

        carryNumber = 0
        ctrlLoop = True
        difference = abs(self.integ.size - other.integ.size)

        while(ctrlLoop):
            temp = int(curr1.data + curr2.data + carryNumber)
            carryNumber = 0
            if temp > 9:
                carryNumber += 1
                temp -= 10
            final.integ.add_first(temp)

            if curr1.prev.data is None or curr2.prev.data is None:
                ctrlLoop = False
            else:
                curr1 = curr1.prev
                curr2 = curr2.prev
        if carryNumber > 0 and difference == 0:
            final.integ.add_first(carryNumber)
            carryNumber = 0
        for i in range(0, difference):
            while(curr1.prev.data != None):
                curr1 = curr1.prev
                temp = curr1.data +carryNumber
                carryNumber = 0
                if temp > 9:
                    carryNumber += 1
                    temp -= 10
                final.integ.add_first(temp)
                # carryNumber = 0
        if carryNumber > 0:
            final.integ.add_first(carryNumber)
        final.integ.delete(final.integ.last_node())
        if final.integ.first_node().data == 0:
            final.integ.delete(final.integ.first_node())
        return final


    def __mul__(self, other):
        testing1 = int(str(self))
        testing2 = int(str(other))

        if testing2 > testing1:
            mult = testing1
        if testing2 < testing1:
            mult = testing1
        final = 0
        for i in range(0, mult):
            final += int(str(other))
        return final


    def __str__(self):
        cursor1 = self.integ.first_node()
        strg = ""
        for i in range(0, len(self.integ)):
            strg = strg + str(cursor1.data)
            cursor1 = cursor1.next
        return strg

    def __repr__(self):
        return str(self)

a = Integer("50")
b = Integer("2")
print(a * b)
#
# print(a + b)