class SListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        new_node = SListNode(item)
        if not self.head or item <= self.head.item:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and item > current.next.item:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, key):
        current = self.head
        prev = None

        while current:
            if current.item == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next

        return False

    def remove_all(self, key):
        removed = False
        current = self.head
        prev = None

        while current:
            if current.item == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = current.next
                removed = True
            else:
                prev = current
                current = current.next

        return removed

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find(self, key):
        current = self.head
        while current:
            if current.item == key:
                return current.item
            current = current.next
        return None

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.item))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __iter__(self):
        current = self.head
        while current:
            yield current.item
            current = current.next

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.item
            count += 1
            current = current.next
        raise IndexError("Index out of range")

# # Example usage and testing
# slist = SList()
# slist.insert(1)
# slist.insert(5)
# slist.insert(6)
# slist.insert(9)
# slist.insert(6)

# print(slist)  # Output: [1, 5, 6, 6, 9]

# slist.remove(5)
# print(slist)  # Output: [1, 6, 6, 9]

# slist.remove_all(6)
# print(slist)  # Output: [1, 9]

# print(slist.size())  # Output: 2

# print(slist.find(1))  # Output: 1
# print(slist.find(9))  # Output: 9
# print(slist.find(5))  # Output: None
