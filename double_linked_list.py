"""
Double Linked List

"""

import gc


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        cur_node = self.head
        while cur_node:
            print("------Linked List Element-----", cur_node.data)
            cur_node = cur_node.next

    def push_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        # By inserting at the beginning now head becomes new node.
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def insert_after(self):
        pass

    def insert_before(self):
        pass

    def delete(self, data):
        if self.head is None:
            print("There is nothing in the linked list to delete.")
            return

        # Linearly search for the data point in the linked list.
        found_data_node = False
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                found_data_node = True
                break
            cur_node = cur_node.next

        if not found_data_node:
            print(f"The data {data} you are looking for is not found.")
            return

        cur_node.prev.next = cur_node.next
        gc.collect()


if __name__ == '__main__':
    ll = LinkedList()

    # linked list is now 3
    ll.push_at_beginning(3)

    # Linked list now becomes 3 -> 4
    ll.append(4)

    # Linked list now becomes 3 -> 4
    ll.append(5)

    # Print the linked List
    ll.print()

    # Delete 4 from list
    ll.delete(4)
    ll.print()

    # Try deleting non existent element from list
    ll.delete(10)
