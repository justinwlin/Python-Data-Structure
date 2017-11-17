def reverseDLL(x):
    firstNode = x.header
    secondNode = x.trailer
    for i in range(0, x.size // 2 + 1):
        tempFirstNode = firstNode.data
        tempSecondNode = secondNode.data

        firstNode.data = tempSecondNode
        secondNode.data = tempSecondNode

        firstNode = firstNode.next
        secondNode = secondNode.prev
    return x


dll = DoublyLinkedList()
dll.add_first(5)
dll.add_first(4)
dll.add_first(3)

print(dll.data)

print(reverseDLL(dll).data)
