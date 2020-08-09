class Queue:
    def __init__(self):
        self.queue = []

    def add(self, x):
        self.queue.append(x)

    def remove(self):
        if len(self.queue)>0:
            last = self.queue[0]
            self.queue.remove(last)
            return last
        else:
            return -1

    def size(self):
        return len(self.queue)

    def traverse(self):
        for item in self.queue:
            print(item)

queue = Queue()
queue.add(12)
queue.add(13)
queue.add(14)
queue.add(15)

print('-----traverse--------')
queue.traverse()

print('------remove---------')
print(queue.remove())

print('-------add 16--------')
queue.add(16)
queue.traverse()

print('------remove---------')
print(queue.remove())

print('-----traverse--------')
queue.traverse()

