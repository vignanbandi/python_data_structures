"""
Queue

Queue is also called FIFO -- First in first out.

RealTime Usage:

1) Queuing Jobs
2) Messaging systems
"""

# TODO: Use collections deque to for good performance.


class Queue:

    def __init__(self, data):
        self.data = data or []

    def enqueue(self, val):
        self.data.append(val)

    def dequeue(self):
        try:
            return self.data.pop(0)
        except IndexError:
            print("Can't dequeue element from queue as its empty")

    def peek(self):
        return self.data[0] if self.data else None

    def print(self):
        print("queue = ", self.data)


if __name__ == "__main__":
    q = Queue(data=[1, 2])

    q.enqueue(7)
    q.enqueue(8)

    print("dequeue element is = ", q.dequeue())
