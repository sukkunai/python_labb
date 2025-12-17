## Лабораторная работа 10

## 1. Краткая теория

### Стек (Stack)
Стек — это структура данных, работающая по принципу "последним пришёл — первым вышел" (LIFO, Last In First Out). Представляет собой список элементов, организованных по принципу LIFO.

**Типичные операции:**
- `push(x)` — добавить элемент (O(1))
- `pop()` — удалить и вернуть верхний элемент (O(1))
- `peek()` — посмотреть верхний элемент без удаления (O(1))

**Типичные применения:**
- история действий (undo/redo);
- обход графа/дерева в глубину (DFS);
- парсинг выражений, проверка скобок.

---

### Очередь (Queue)
Очередь — это структура данных, работающая по принципу "первым пришёл — первым вышел" (FIFO, First In First Out).
Представляет собой список элементов, организованных по принципу FIFO.

**Типичные операции:**
- `enqueue(x)` — добавить элемент (O(1))
- `dequeue()` — удалить и вернуть первый элемент (O(1))
- `peek()` — посмотреть первый элемент (O(1))

**Типичные применения:**
- обработка задач по очереди (job queue);
- обход графа/дерева в ширину (BFS);
- буферы (сетевые, файловые, очереди сообщений).

---

### Односвязный список (Singly Linked List)
Список состоит из узлов `Node`, где каждый узел содержит:
- значение (`value`)
- ссылку на следующий узел (`next`)

**Типичные операции:**
- `append(x)` — добавить в конец (O(n) или O(1) при хвосте)
- `prepend(x)` — добавить в начало (O(1))
- `insert(i, x)` — вставить по индексу (O(n))
- `remove(value)` — удалить элемент по значению — (O(n))
- `remove_at(idx)` — удалить элемент по индексу — (O(n))

**Преимущества:**
- Динамический размер
- Эффективная вставка и удаление в начале — (O(1))

**Недостатки:**
- Доступ к элементу по индексу — (O(n))
- Дополнительная память на хранение указателей

### Задание A
```python

from collections import deque

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Пустой стек')
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class Queue:

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Пустая очередь')
        return self._data.popleft()

    def peek(self):
        if not self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

print('===Stack===')
stack = Stack()
print(f'Пустой стек: {stack.is_empty()}')
stack.push(10)
stack.push(20)
stack.push(30)
print(f'размер стека после добавления 3 элементов: {len(stack)}')
print(f'верхний элемент (peek): {stack.peek()}')
print(f'удаляем {stack.pop()}') 
print(f'удаляем {stack.pop()}') 
print(f'оставшийся размер: {len(stack)}') 
while not stack.is_empty():
    print(f'удаляем: {stack.pop()}')
print(f'cтек пустой: {stack.is_empty()}')
print(f'peek из пустого стека: {stack.peek()}')
try:
    stack.pop()
except IndexError as e:
    print(f'ошибка при удалении из пустого стека: {e}')

print('===Queue===')
queue = Queue()
print(f'пустая очередь: {queue.is_empty()}')
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f'размер очереди после добавления 3 элементов: {len(queue)}')
print(f'первый элемент: {queue.peek()}') 
print(f'удаляем (dequeue): {queue.dequeue()}') 
print(f'удаляем (dequeue): {queue.dequeue()}')
print(f'оставшийся размер: {len(queue)}')
while not queue.is_empty():
    print(f'удаляем {queue.dequeue()}')
print(f'очередь пустая: {queue.is_empty()}')
try:
    queue.dequeue()
except IndexError as e:
    print(f'ошибка при dequeue из пустой очереди: {e}')

```
![Картинка 1](./images/lab10/st.png)

### Задание B 
```python

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

```
![Картинка 2](./images/lab10/ll.png)


### Выводы по бенчмаркам

Стек — самая быстрая структура данных:
 - Реализация на базе списка Python (list)
 - append() и pop() работают за амортизированное O(1)
 - Минимальные накладные расходы

Очередь — немного медленнее стека:
 - Использует deque из collections
 - append() и popleft() работают за O(1)
 - Все ещё значительно быстрее связных списков

Односвязный список — самая медленная из трёх:
 - Каждая операция требует создания объекта Node
 - Нет локальности данных (разрозненное хранение в памяти)
 - Много операций с указателями
 - Для удаления элемента по индексу требуется O(n) операций