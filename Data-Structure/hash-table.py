from functools import reduce
from operator import add


class LinkedListNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.item_count = 0

    def hash(self, value):
        byte_value = value.encode()
        sum_bytes = reduce(add, byte_value)
        return sum_bytes % self.capacity

    def get_load_factor(self):
        return self.item_count / self.capacity

    def resize(self):
        self.item_count = 0
        old_storage = self.storage
        new_capacity = self.capacity * 2
        self.capacity = new_capacity
        self.storage = [None] * self.capacity
        for slot in old_storage:
            current_node = slot
            while current_node:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next

    def put(self, key, value):
        index = self.hash(key)
        new_node = LinkedListNode(key, value)
        if self.storage[index] is not None:
            current_head = self.storage[index]
            new_node.next = current_head
            self.storage[index] = new_node
        else:
            self.storage[index] = new_node
        self.item_count += 1

        if self.get_load_factor() > 0.7:
            self.resize()

    def get(self, key):
        index = self.hash(key)
        current_node = self.storage[index]
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        print(f'The key {key} does not exist')
        return None

    def remove(self, key):
        index = self.hash(key)
        self.storage[index] = None
        self.item_count -= 1

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


my_dic = HashTable(4)

my_dic['apple'] = 'apple is a fruit'
my_dic['banana'] = 'banana is a fruit'
my_dic['peach'] = 'peach is a fruit'
my_dic['cucumber'] = 'vegetable'
my_dic['tomato'] = 'tomato is a fruit'
my_dic['watermelon'] = 'watermelon is a berry'

print(my_dic['apple'])
print(my_dic['banana'])
print(my_dic['peach'])
