class SListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class SList:
    def __init__(self):
        self._head = None

    def insert(self, item):
        new_node = SListNode(item)
        if not self._head or item <= self._head.item:
            new_node.next = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next and item > current.next.item:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, key):
        if not self._head:
            return False
        if self._head.item == key:
            self._head = self._head.next
            return True
        current = self._head
        while current.next and current.next.item != key:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False

    def remove_all(self, key):
        if not self._head:
            return
        while self._head and self._head.item == key:
            self._head = self._head.next
        current = self._head
        while current and current.next:
            if current.next.item == key:
                current.next = current.next.next
            else:
                current = current.next

    def size(self):
        count = 0
        current = self._head
        while current:
            count += 1
            current = current.next
        return count

    def find(self, key):
        current = self._head
        while current:
            if current.item == key:
                return current.item
            current = current.next
        return None

    def __str__(self):
        result = '['
        current = self._head
        while current:
            result += str(current.item)
            if current.next:
                result += ', '
            current = current.next
        return result + ']'

    def __iter__(self):
        self.current = self._head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        item = self.current.item
        self.current = self.current.next
        return item

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        current = self._head
        while current and index > 0:
            current = current.next
            index -= 1
        if not current:
            raise IndexError("Index out of range")
        return current.item

    def __len__(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next
        return count



# Example usage:
slist = SList()
slist.insert(3)
slist.insert(1)
slist.insert(2)

print(slist)  # Output: [1, 2, 3]

for item in slist:
    print(item)  # Output: 1, 2, 3

print(slist[1])  # Output: 2
