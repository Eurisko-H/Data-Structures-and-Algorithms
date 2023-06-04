class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_at_head(link_list, value):
    new_node = LinkListNode(value)
    new_node.next = link_list
    return new_node


def insert_at_tail(link_list_tail, value):
    new_tail = LinkListNode(value)
    link_list_tail.next = new_tail
    return new_tail


def print_list_recursive(start_node):
    if start_node:
        print(start_node.value)
        print_list_recursive(start_node.next)


head = LinkListNode(6)
tail = head

head = insert_at_head(head, 5)
head = insert_at_head(head, 4)
head = insert_at_head(head, 3)

tail = insert_at_tail(tail, 7)

# print_list_recursive(head)

"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:
The code below should first construct a linked list(x -> y -> z) and
then delete 'y' from the linked list by calling the function 'delete_node'.
It is your job to write the 'delete_node' function.

Note: we can do this in O(1) time and space! But be aware out solution will have some side effects...
"""


def delete_node(delete_this_node):
    next_node = delete_this_node.next
    if next_node is None:
        print("can't do it, can't delete last node")
    else:
        delete_this_node.value = next_node.value
        delete_this_node.next = next_node.next


x = LinkListNode('x')
y = LinkListNode('y')
z = LinkListNode('z')

x.next = y
y.next = z

delete_node(y)
# print_list_recursive(x)


"""
Given a reference to the head of a singly-linked list, write a function
that reverses the linked list in place, The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you can't make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list once.
"""


# BigO -> O(n)
def reverse(head_of_list):
    prev_node = None
    curr_node = head_of_list
    next_node = head_of_list.next
    while curr_node is not None:
        next_node = curr_node.next

        curr_node.next = prev_node

        prev_node = curr_node
        curr_node = next_node
    return prev_node


a = LinkListNode('a')
b = LinkListNode('b')
c = LinkListNode('c')

a.next = b
b.next = c

# print_list_recursive(a)
# new_head = reverse(a)
# print_list_recursive(new_head)


# https://leetcode.com/problems/linked-list-cycle/?envType=list&envId=rohd04ig

def has_cycle(link_list) -> bool:
    # Floyd's Tortoise and Hare algorithm
    slow, fast = link_list, link_list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
