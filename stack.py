"""
Stack

Stack is also called LIFO -- Last in first out.

Real Time usage:
1) Error traceback uses stacks,
2) Browser back tracking: Each page u visit it will be added to the stack and enables you to go back in LIFO order.
"""


class Stack:

    def __init__(self, data):
        self.data = data or []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            print("Can't pop element from stack as its empty")

    def peek(self):
        return self.data[0] if self.data else None

    def print(self):
        print("stack = ", self.data)


if __name__ == "__main__":
    st = Stack(data=[1, 2])

    st.push(7)
    st.push(8)

    print("Poped element is = ", st.pop())
