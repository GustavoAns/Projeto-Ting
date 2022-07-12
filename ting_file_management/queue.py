from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def search(self, index):
        max_len = len(self._data)
        if index < 0 or index >= max_len:
            raise IndexError('Index fora de alcance')
        return self._data[index]
