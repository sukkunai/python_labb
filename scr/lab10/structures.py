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