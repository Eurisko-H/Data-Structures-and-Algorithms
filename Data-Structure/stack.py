class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Stack using the Linked-List:
- The BigO of insert & remove & access is O(1)
"""


class LLStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = LinkListNode(value)
        new_node.next = self.top

        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        old_top = self.top
        self.top = old_top.next

        return old_top.value


my_stack = LLStack()

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')

# print(f"The top of the stack is {my_stack.top.value}")
# print(f"Remove the value from the top")
# print(f"removed value is {my_stack.pop()}")
# print(f"The top of the stack is {my_stack.top.value}")


"""
Stack using the Array:
- The BigO of insert & remove is O(n) 
- But accessing is O(1)
"""


class AStack:
    def __init__(self):
        self.item = []

    def push(self, value):
        self.item.append(value)

    def pop(self):
        if not self.item:
            return None
        return self.item.pop()

    def peek(self):
        if not self.item:
            return None
        return self.item[-1]

    def empty(self):
        return True if len(self.item) == 0 else False


stack = AStack()

stack.push('A')
stack.push('B')
stack.push('C')

# print(f"The top of the stack is {stack.peek()}")
# print(f"Remove the value from the top")
# print(f"removed value is {stack.pop()}")
# print(f"The top of the stack is {stack.peek()}")


def valid_bracket_sequence(symbol: str) -> bool:
    s = AStack()
    close_to_open = {')': '(', '}': '{', ']': '['}
    for c in symbol:
        if c in close_to_open:
            if not s.empty() and close_to_open[c] == s.peek():
                s.pop()
            else:
                return False
        else:
            s.push(c)
    return True if s.empty() else False
