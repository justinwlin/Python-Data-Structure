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

class CompactString:
    def __init__(self, num_str):
        self.comStr = DoublyLinkedList()
        counter = 0
        index1 = 0
        for index2 in range(0, len(num_str)):
            if num_str[index1] == num_str[index2]:
                counter += 1
            else:
                self.comStr.add_last((num_str[index1], counter))
                index1 = index2
                counter = 1
        self.comStr.add_last((num_str[index1], counter))


    def __add__(self, other):
        if self.comStr.is_empty():
            return other.comStr
        if other.comStr.is_empty():
            return self.comStr
        final = DoublyLinkedList()
        cursor = self.comStr.last_node()
        cursorOther = other.comStr.first_node()

        compare1 = cursor.data[0]
        compare2 = cursorOther.data[0]

        compare1Num = cursor.data[1]
        compare2Num = cursorOther.data[1]

        if compare1 == compare2:
            temp = compare1Num + compare2Num
            tempV = compare1
            self.comStr.delete(self.comStr.last_node())
            self.comStr.add_last((tempV, temp))
            other.comStr.delete(other.comStr.first_node())
        for i in self.comStr:
            final.add_last(i)
        for k in other.comStr:
            final.add_last(k)
        string = ""
        for item in final:
            for j in range(item[1]):
                string += item[0]
        return CompactString(string)

    def __lt__(self, other):
        ctrlLoop = True
        while ctrlLoop:
            if len(self.comStr) == 0 and len(other.comStr) > 0:
                return True
            if len(other.comStr) == 0 and len(self.comStr) > 0:
                return False
            if len(other.comStr) == 0 and len(self.comStr) == 0:
                return False
            compare1 = self.comStr.first_node()
            compare2 = other.comStr.first_node()
            
            compare1Value = compare1.data[0]
            compare2Value = compare2.data[0]

            if compare1Value == compare2Value:
                temp1 = self.comStr.first_node().data[1]
                temp2 = other.comStr.first_node().data[1]
                if temp1 == temp2: #DELETE THE TEMP1 and TEMP2
                    self.comStr.delete(self.comStr.first_node())
                    other.comStr.delete(other.comStr.first_node())
                elif temp1 < temp2:
                    self.comStr.delete(self.comStr.first_node())
                    other.comStr.delete(other.comStr.first_node())
                    tupleTemp = (compare1, temp2 - temp1)
                    other.comStr.add_first(tupleTemp)
                elif temp1 > temp2:
                    other.comStr.delete(other.comStr.first_node())
                    self.comStr.delete(self.comStr.first_node())
                    tupleTemp = (compare1, temp2 - temp1)
                    self.comStr.add_first(tupleTemp)
            elif compare1Value > compare2Value:
                return False
            elif compare1Value < compare2Value:
                return True

    def __le__(self, other):
        ctrlLoop = True
        while ctrlLoop:
            if len(self.comStr) == 0 and len(other.comStr) > 0:
                return True
            if len(other.comStr) == 0 and len(self.comStr) > 0:
                return False
            if len(other.comStr) == 0 and len(self.comStr) == 0:
                return True
            compare1 = self.comStr.first_node()
            compare2 = other.comStr.first_node()

            compare1Value = compare1.data[0]
            compare2Value = compare2.data[0]

            if compare1Value == compare2Value:
                temp1 = self.comStr.first_node().data[1]
                temp2 = other.comStr.first_node().data[1]
                if temp1 == temp2: #DELETE THE TEMP1 and TEMP2
                    self.comStr.delete(self.comStr.first_node())
                    other.comStr.delete(other.comStr.first_node())
                elif temp1 < temp2:
                    self.comStr.delete(self.comStr.first_node())
                    other.comStr.delete(other.comStr.first_node())
                    tupleTemp = (compare1, temp2 - temp1)
                    other.comStr.add_first(tupleTemp)
                elif temp1 > temp2:
                    other.comStr.delete(other.comStr.first_node())
                    self.comStr.delete(self.comStr.first_node())
                    tupleTemp = (compare1, temp2 - temp1)
                    self.comStr.add_first(tupleTemp)
            elif compare1Value > compare2Value:
                return False
            elif compare1Value < compare2Value:
                return True

    def __gt__(self, other):
        ctrlLoop = True
        while ctrlLoop:
            if len(self.comStr) == 0 and len(other.comStr) > 0:
                return False
            if len(other.comStr) == 0 and len(self.comStr) > 0:
                return True
            if len(other.comStr) == 0 and len(self.comStr) == 0:
                return False
            compare1 = self.comStr.first_node()
            compare2 = other.comStr.first_node()

            compare1Value = compare1.data[0]
            compare2Value = compare2.data[0]

            if compare1Value == compare2Value:
                temp1 = self.comStr.first_node().data[1]
                temp2 = other.comStr.first_node().data[1]
                if temp1 == temp2:  # DELETE THE TEMP1 and TEMP2
                    self.comStr.delete(self.comStr.first_node())
                    other.comStr.delete(other.comStr.first_node())
                elif temp1 < temp2:
                    self.comStr.delete(self.comStr.first_node())
                    other.comStr.delete(other.comStr.first_node())
                    tupleTemp = (compare1, temp2 - temp1)
                    other.comStr.add_first(tupleTemp)
                elif temp1 > temp2:
                    other.comStr.delete(other.comStr.first_node())
                    self.comStr.delete(self.comStr.first_node())
                    tupleTemp = (compare1, temp2 - temp1)
                    self.comStr.add_first(tupleTemp)
            elif compare1Value < compare2Value:
                return False
            elif compare1Value > compare2Value:
                return True

    def __ge__(self, other):
        ctrlLoop = True
        while ctrlLoop:
            if len(self.comStr) == 0 and len(other.comStr) > 0:
                return False
            if len(other.comStr) == 0 and len(self.comStr) > 0:
                return True
            if len(other.comStr) == 0 and len(self.comStr) == 0:
                return True
            compare1 = self.comStr.first_node()
            compare2 = other.comStr.first_node()

            compare1Value = compare1.data[0]
            compare2Value = compare2.data[0]


            if compare1Value == compare2Value:
                temp1 = self.comStr.first_node().data[1]
                temp2 = other.comStr.first_node().data[1]
                if temp1 == temp2:  # DELETE THE TEMP1 and TEMP2
                    self.comStr.delete(self.comStr.first_node())
                    other.comStr.delete(other.comStr.first_node())
                elif temp1 < temp2:
                    self.comStr.delete(self.comStr.first_node())
                    other.comStr.delete(other.comStr.first_node())
                    tupleTemp = (compare1, temp2 - temp1)
                    other.comStr.add_first(tupleTemp)
                elif temp1 > temp2:
                    other.comStr.delete(other.comStr.first_node())
                    self.comStr.delete(self.comStr.first_node())
                    tupleTemp = (compare1, temp2 - temp1)
                    self.comStr.add_first(tupleTemp)
            elif compare1Value < compare2Value:
                return False
            elif compare1Value > compare2Value:
                return True

    def __str__(self):
        string = ""
        for item in self.comStr:
            for j in range(item[1]):
                string += item[0]
        return string

    def __repr__(self):
        return str(self)
#
# a = CompactString("a")
# b = CompactString("abba")
# print(a < b)
# # # # print(b)
# # # # print(a + b)
# # #
# # print(a < b)
# # # # print(a <= b)
# # # #
# # # # print(b > a)
# # # # print(b >= a)