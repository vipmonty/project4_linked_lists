# SList.py

class SListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        """
        Inserts an item into the list at the appropriate location to maintain ascending order.
        """
        new_node = SListNode(item)
        if self.head is None or item < self.head.item:
            # Insert at the beginning if the list is empty or the item is smaller than the head
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.item < item:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, key):
        """
        Removes the first occurrence of an item indicated by the key from the list.
        Returns True if an item was found and removed, False if not.
        """
        if self.head is None:
            return False

        if self.head.item == key:
            self.head = self.head.next
            return True

        current = self.head
        while current.next is not None:
            if current.next.item == key:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def remove_all(self, key):
        """
        Removes all occurrences of an item indicated by the key from the list.
        """
        if self.head is None:
            return

        while self.head is not None and self.head.item == key:
            self.head = self.head.next

        current = self.head
        while current is not None and current.next is not None:
            if current.next.item == key:
                current.next = current.next.next
            else:
                current = current.next

    def size(self):
        """
        Returns the current number of items/nodes in the list.
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def find(self, key):
        """
        Searches for the first occurrence of an item indicated by the key value in the list.
        If found, the item is returned; returns None otherwise.
        """
        current = self.head
        while current is not None:
            if current.item == key:
                return current.item
            current = current.next
        return None

    def __str__(self):
        """
        Returns a string representation of the contents of the list.
        """
        if self.head is None:
            return '[]'

        result = '['
        current = self.head
        while current is not None:
            result += str(current.item)
            if current.next is not None:
                result += ', '
            current = current.next
        result += ']'
        return result

    def __iter__(self):
        """
        Returns an iterator object to make the list iterable.
        """
        current = self.head
        while current is not None:
            yield current.item
            current = current.next

    def __getitem__(self, index):
        """
        Returns the value stored at position index in the list.
        """
        if index < 0:
            raise IndexError("Index out of range")

        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.item
            count += 1
            current = current.next

        raise IndexError("Index out of range")