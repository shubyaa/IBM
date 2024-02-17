class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data=data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
    
    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)

        print(elements)
    

    def insertNodeAtIndex(self, data, index):
        newNode = Node(data=data)

        current_node = self.head
        position = 0

        if self.length() == index:
            self.append(data)
        else:
            while current_node != None and position != index:
                position += 1
                current_node = current_node.next

            if current_node != None:
                newNode.next = current_node.next 
                current_node.next = newNode
            else:
                print("ERROR: Index Not present")

    

new_list = linked_list()

new_list.append(2)
new_list.append(3)
new_list.append(4)
new_list.append(5)
new_list.append(1)
new_list.append(3)
new_list.append(2)

new_list.insertNodeAtIndex(69, 1)

new_list.display()