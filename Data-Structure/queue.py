class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Queue using the Linked-List:
- The BigO of insert & remove & access is O(n)
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
