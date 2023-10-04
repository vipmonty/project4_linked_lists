# SList.py

class SListNode:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class SList:
    def __init__(self):
        self._head = None
        self.size

    def insert(self, value):
        """
        Inserts an value into the list at the appropriate location to maintain ascending order.
        """
        new_node = SListNode(value)
        if self._head is None or value < self._head.value:
            # Insert at the beginning if the list is empty or the value is smaller than the _head
            new_node.next = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next is not None and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node



    def size(self):
        """
        Returns the current number of items/nodes in the list.
        """
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next
        return count

    def find(self, key):
        """
        Searches for the first occurrence of an value indicated by the key value in the list.
        If found, the value is returned; returns None otherwise.
        """
        current = self._head
        while current is not None:
            if current.value == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        """
        Removes the first occurrence of an value indicated by the key from the list.
        Returns True if an value was found and removed, False if not.
        """
        if self._head is None:
            return False

        if self._head.value == key:
            self._head = self._head.next
            return True

        current = self._head
        while current.next is not None:
            if current.next.value == key:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def remove_all(self, key):
        """
        Removes all occurrences of an value indicated by the key from the list.
        """
        if self._head is None:
            return

        while self._head is not None and self._head.value == key:
            self._head = self._head.next

        current = self._head
        while current is not None and current.next is not None:
            if current.next.value == key:
                current.next = current.next.next
            else:
                current = current.next

    def __str__(self):
        """
        Returns a string representation of the contents of the list.
        """
        if self._head is None:
            return '[]'

        result = '['
        current = self._head
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += ', '
            current = current.next
        result += ']'
        return result

    def __iter__(self):
        """
        Returns an iterator object to make the list iterable.
        """
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __getitem__(self, index):
        """
        Returns the value stored at position index in the list.
        """
        if index < 0:
            raise IndexError("Index out of range")

        current = self._head
        count = 0
        while current is not None:
            if count == index:
                return current.value
            count += 1
            current = current.next

        raise IndexError("Index out of range")
    
    def __len__(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next
        return count