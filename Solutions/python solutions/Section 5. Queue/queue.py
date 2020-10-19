class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) > 0:
            return False
        else: 
            return True

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("no data in queue")
        else:
            return self.queue.pop(0)

    def display(self):
        for item in self.queue:
            print(item, end = ' ')

q = Queue()
print('enqueue <value>')
print('dequeue')
print('quit')
while True:
    print('The Queue: ', end = '')
    q.display()

    print()
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        print(int(do[1]))
        q.enqueue(int(do[1]))
    elif operation == 'dequeue':
        print('Dequeued value: ', q.dequeue())
    elif operation == 'quit':
        break