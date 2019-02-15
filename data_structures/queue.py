class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
       self.queue.insert(0, item)
       return self.queue

    def dequeue(self):
       if self.isEmpty():
           return 'Queue empty'
       return self.queue.pop()

    def size(self):
       return len(self.queue)

    def isEmpty(self):
       return len(self.queue) == 0


