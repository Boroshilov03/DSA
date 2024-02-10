#Linked List
#Insert Element at beginning = O(1)
#Delete Element at beginning = O(1)
#Insert/Delete Element At the End = O(n)
#Linked List Traversal = O(n)
#Accessing Element By Value = O(n)

#Benefits over an array:
#1. You don't need to pre-allocate space
#2. Insertion is easier

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self): #empty linked list
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("List is empty")

        itr = self.head
        llstr =''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def inserting_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.inserting_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr.next:
            count+=1
            itr = itr.next

        return count
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid index")

        if index ==0:
            self.head = self.head.next
            return #Python takes care of garbage collection, unlike, c++ (explicitly have to the remove from the memory)

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next #skipping over a node
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

ll = LinkedList()
# ll.insert_at_beginning(5)
# ll.insert_at_beginning(89)
# ll.inserting_at_end(11)
ll.insert_values(["cherry", "orange"])
# ll.remove_at(0)
ll.insert_at(0, "kiwi")
ll.insert_at(2, "watermelon")
ll.insert_after_value("watermelon", "grapes")
ll.remove_by_value("orange")

ll.print()

