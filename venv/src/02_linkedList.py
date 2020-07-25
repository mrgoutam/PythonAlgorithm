"""
A linked list is a sequence of data elements, which are connected together via links.
Each data element contains a connection to another data element in form of a pointer
"""

# structure of node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def insertAtBeginning(self, x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode

    def insertAtLast(self, x):
        newNode = Node(x)
        node = self.head

        # linked list is empty
        if node is None:
            self.head = newNode
            return

        while node.next:
            node = node.next
        node.next = newNode

    def insertInBetween(self, x, position):
        if position<0:
            print("Please insert a valid index")
            return
        elif position>self.length():
            print("index is out of bound")
            return
        newNode = Node(x)
        node = self.head
        count = 0
        while count<position-1:
            count += 1
            node = node.next
        secondPart = node.next
        node.next = newNode
        newNode.next = secondPart

    def removeByKey(self):
        pass
    def removeByIndex(self):
        pass

    def length(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

def showDetails(lLinked, message):
    print('------', message, '------')
    lLinked.traverse()
    print('Length: ', ll.length())
ll = LinkedList() # first node without value
ll.head = Node('21') # inserting value to first or head node

# two independent node
node2 = Node('24')
node3 = Node('12')

# linking second node to first node
ll.head.next = node2

# linking third node to second node
node2.next = node3

# traversing linked list
showDetails(ll, 'Just started')

ll.insertAtBeginning('50')
showDetails(ll, 'inserted 50 at beginning')

ll.insertAtLast('100')
showDetails(ll, 'inserted 100 at last')

ll.insertInBetween('75', 2)
showDetails(ll, 'inserted 75 at position 2')

