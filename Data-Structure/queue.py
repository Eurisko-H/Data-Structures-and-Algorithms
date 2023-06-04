class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Queue using the Linked-List:
- The BigO of insert & remove & access is O(1)
"""


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = LinkListNode(value)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None

        old_front = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return old_front.value


my_queue = Queue()

my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')

# print(f"The front of the queue is {my_queue.front.value}")
# print(f"Remove the value from the front")
# print(f"removed value is {my_queue.dequeue()}")
# print(f"The front of the queue is {my_queue.front.value}")


"""
Your goal is to define a 'Queue' class that uses two stacks. Your 'Queue' class
should have an 'enqueue()' method and a 'dequeue()' method that ensures a 
"first in first out (FIFO) order"

As you write your methods, you should optimize for time on the 'enqueue()' and
'dequeue()' method calls.

The Stack class that you will use has been provided to you.
"""


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"


class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if len(self.out_stack.data) == 0:
            while len(self.in_stack.data) > 0:
                popped_item = self.in_stack.pop()
                self.out_stack.push(popped_item)
        return self.out_stack.pop()
