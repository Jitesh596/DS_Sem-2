# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__ (self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

def main():
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_beginning(5)
    sll.insert_at_beginning(1)
    print("List after insertions:")
    sll.traverse()
    sll.delete_by_value(20)
    print("List after deletion of 20:")
    sll.traverse()
if __name__ == "__main__":
    main()
