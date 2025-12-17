class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next 


class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None 
        self.tail: Node | None = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node

        if current == self.tail:
            self.tail = new_node

        self._size += 1 

    def remove(self, value):
        if self.head is None:
            return 

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is not None:
            current.next = current.next.next
            self._size -= 1
            if current.next is None:
                self.tail = current

    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size - 1}]")

        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            if self.head is None: 
                self.tail = None
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        current.next = current.next.next
        self._size -= 1

        if current.next is None:
            self.tail = current

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

    

lst = SinglyLinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)
print(len(lst))
lst.prepend(0)
print(lst)
lst.insert(2, 99)
print(lst)  
lst.insert(5, 100)
print(lst)
lst.remove(99)
print(lst)
lst.remove_at(0)
print(lst)
print(len(lst)) 
print(lst.tail.value if lst.tail else None) 