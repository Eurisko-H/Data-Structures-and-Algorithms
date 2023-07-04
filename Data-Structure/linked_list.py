# https://www.youtube.com/watch?v=FLNYOxQp5zc&list=PLWX9jswdDQ0Ve8375p6yejDJu3668zxnV&index=5&pp=iAQB&ab_channel=BloomInstituteofTechnology
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_at_head(link_list, value):
    new_node = LinkedListNode(value)
    new_node.next = link_list
    return new_node


def insert_at_tail(link_list_tail, value):
    new_tail = LinkedListNode(value)
    link_list_tail.next = new_tail
    return new_tail


def print_list_recursive(start_node):
    if start_node:
        print(start_node.value)
        print_list_recursive(start_node.next)


head = LinkedListNode(6)
tail = head
head = insert_at_head(head, 4)
head = insert_at_head(head, 3)
tail = insert_at_tail(tail, 7)

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


"""
You have a single linked list L, which is sorted in strictly increasing order, and a integer value.
Add value to the list L, preserving its original sorting

Notes:
1- Your solution should have O(n) time complexity
2- in the example below the linked list presented as array for simplicity

Example:
- l = [1, 3, 4, 6] value = 5 -> output: [1, 2, 4, 5, 6]   # In the middle
- l = [1, 3, 4, 6] value = 10 -> output: [1, 2, 4, 6, 10] # In the end
- l = [1, 3, 4, 6] value = 0 -> output: [0, 1, 2, 4, 6]   # In the start
"""


def insert_value_into_sorted_linked_list(linked_list, value):
    current_node = linked_list
    new_node = Node(value)
    # if the linked list is empty
    if linked_list is None:
        return new_node
    # if the value is smaller than the linked list head
    if new_node.data < current_node.value:
        new_node.next = current_node
        return new_node
    while current_node.next:
        next_node = current_node.next
        if next_node.value > new_node.data:
            current_node.next = new_node
            new_node.next = next_node
            return linked_list
        else:
            current_node = current_node.next
    # add the node to end of our list
    current_node.next = new_node
    return linked_list


# https://leetcode.com/problems/merge-two-sorted-lists/?envType=list&envId=rohd04ig
def merge_two_sorted_list(l1, l2):
    dummy_node = Node(None)
    tail = dummy_node
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy_node.next


# https://leetcode.com/problems/remove-linked-list-elements/
def remove_element(head, val: int):
    dummy_node = Node(None)
    dummy_node.next = head
    prev_node, curr_node = dummy_node, head
    while curr_node:
        if curr_node.data == val:
            prev_node.next = curr_node.next
        else:
            prev_node = curr_node
        curr_node = curr_node.next
    return dummy_node.next
    """______OR______"""
    prev_node, curr_node = None, head
    while curr_node:
        if curr_node.data == val:
            if head == curr_node:
                head = curr_node.next
            else:
                prev_node.next = curr_node.next
        else:
            prev_node = curr_node
        curr_node = curr_node.next
    return head


# https://leetcode.com/problems/odd-even-linked-list/
def odd_even_list(head):
    odd_node = Node(None)
    odd_tail = odd_node
    even_node = Node(None)
    even_tail = even_node

    index = 1
    current_node = head

    while current_node:
        if index % 2 == 1:
            odd_tail.next = current_node
            odd_tail = odd_tail.next
        else:
            even_tail.next = current_node
            even_tail = even_tail.next

        current_node = current_node.next
        index += 1

    if odd_tail:
        odd_tail.next = None
    if even_tail:
        even_tail.next = None

    odd_tail.next = even_node.next
    return odd_node.next


# Linked-List implementation With Rob CS310 at San Diego State University
# https://www.youtube.com/watch?v=rxpUg4M_jWo&list=PLpPXw4zFa0uKKhaSz87IowJnOTzh9tiBk&index=13
"""LinkedList 3 Boundary Conditions
- Empty data structure
- Single element in the data structure
- Adding / removing beginning of data structure
- Adding / removing end of the data structure
- Working in the middle
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return LinkedListIterator(self.head)

    def add_first(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def add_last(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def print_list(self):
        if self.head is None:
            print('Empty')
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end='->')
            current_node = current_node.next
        print()

    def remove_first(self):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return
        temp = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = self.head
        else:
            self.head = self.head.next
        self.length -= 1
        return temp

    def remove_last(self):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return
        if self.head == self.tail:
            return self.remove_first()
        prev_node, current_node = None, self.head
        while current_node != self.tail:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None
        self.tail = prev_node
        self.length -= 1
        return current_node.data

    def reverse(self):
        # https://leetcode.com/problems/reverse-linked-list/?envType=list&envId=rohd04ig
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return
        if self.head == self.tail:
            print('Only one element, No need to reverse')
            return
        prev_node = None
        current_node = self.head
        self.tail = current_node
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def remove_and_find(self, val):
        current, prev = self.head, None
        if self.head.data == val:
            return self.remove_first()
        if self.tail.data == val:
            return self.remove_last()
        while current:
            if current.data == val:
                self.length -= 1
                prev.next = current.next
                return current.data
            prev = current
            current = current.next
        return None

    """
    -Stop at last node -> while (temp.next != None)
    -Past the last node -> while (temp != None) 
    """

    def peek_first(self):
        if self.head is None:
            return None
        return self.head.data

    def peek_last(self):
        if self.tail is None:
            return None
        return self.tail.data

    def has_cycle(self):
        # https://leetcode.com/problems/linked-list-cycle/?envType=list&envId=rohd04ig
        # Floyd's cycle detection algorithm (Tortoise and hare)
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def palindrome(self, val) -> bool:
        pass
