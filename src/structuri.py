class StackOnList():
    """
       Реализация стека на списках
    """
    def __init__(self):
        """
            Инициализация пустого стека
        """
        self.stack = []
    def push(self, x):
        """
            Добавляет элемент на вершину стека
        """
        if not self.stack:
            current_min = x
        else:
            current_min = min(x, self.stack[-1][1])
        self.stack.append((x, current_min))
    def pop(self):
        """
            Удаляет  элемент с вершины стека
        """
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Empty stack")
    def peek(self):
        """
        Возвращает элемент с вершины стека без его удаления
        """
        if not self.is_empty():
            return self.stack[-1][0]
        raise IndexError("Empty stack")
    def is_empty(self):
        """
            Проверяет, пуст ли стек
        """
        return len(self.stack) == 0

    def __len__(self):
        """
            Возвращает количество элементов в стеке
        """
        return len(self.stack)

    def getMin(self) -> int:
        """
            Возвращает минимальный элемент в стеке
        """
        if self.stack:
            return self.stack[-1][1 ]
        raise IndexError("Empty stack")

class QueueOnList:
    """
       Реализация очереди на списках
    """
    def __init__(self):
        """
            Инициализация пустой очереди
        """
        self.queue = []
    def enqueue(self, x):
        """
             Добавляет элемент в конец очереди
        """
        self.queue.append(x)
    def dequeue(self):
        """
            Удаляет и возвращает элемент из начала очереди
        """
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Empty queue")

    def front(self):
        """
                Возвращает элемент из начала очереди без его удаления
        """
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Empty queue")

    def is_empty(self):
        """
            Проверяет пуста ли очередь
        """
        return len(self.queue) == 0
    def __len__(self):
        """
            Возвращает количество элементов в очереди
        """
        return len(self.queue)