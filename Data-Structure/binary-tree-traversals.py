class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Run_time: O(n) - Space_complexity: O(n)
    def print_tree_pre_order(self):
        # Evaluate the current node
        print(self.value)
        if self.left is not None:
            self.left.print_tree_pre_order()
        if self.right is not None:
            self.right.print_tree_pre_order()

    def print_tree_in_order(self):
        if self.left is not None:
            self.left.print_tree_in_order()
        # Evaluate the current node
        print(self.value)
        if self.right is not None:
            self.right.print_tree_in_order()

    def print_tree_post_order(self):
        if self.left is not None:
            self.left.print_tree_post_order()
        if self.right is not None:
            self.right.print_tree_post_order()
        # Evaluate the current node
        print(self.value)

    # Run_time: O(n) - Space: O(n)
    # Depth first traversal
    def print_tree_iterative_dft(self):
        stack = [self]
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)

    # Breadth first traversal
    def print_tree_iterative_bft(self):
        queue = [self]
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    all_paths = []

    def find_path_to_leaves(self, current_path):
        new_path = current_path + [self.value]
        if self.left is None and self.right is None:
            self.all_paths.append(new_path)

        if self.left is not None:
            self.left.find_path_to_leaves(new_path.copy())

        if self.right is not None:
            self.right.find_path_to_leaves(new_path.copy())


root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(9)

root.print_tree_iterative_dft()
# root.print_tree_iterative_bft()


root.find_path_to_leaves(current_path=[])
print(root.all_paths)
