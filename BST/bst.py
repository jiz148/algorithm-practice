"""
BST algorithms
"""


class Node:

    def __init__(self, value):
        self.val, self.left, self.right = value, None, None


class BST:

    def __init__(self, array):
        self.root = Node(array.pop(0))
        self.build(array)

    def build(self, array):
        while len(array) != 0:
            self.insert(self.root, array.pop(0))

    def insert(self, node, value):
        if not node.left and not node.right:
            if value < node.val:
                node.left = Node(value)
            else:
                node.right = Node(value)
            return
        if value < node.val:
            if node.left:
                self.insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.insert(node.right, value)
            else:
                node.right = Node(value)

    def show(self):
        queue = [self.root]
        while len(queue) != 0:
            values = []
            next_queue = []
            for item in queue:
                values.append(item.val)
                if item.left:
                    next_queue.append(item.left)
                if item.right:
                    next_queue.append(item.right)
            print(values)
            queue = next_queue

    def search(self, value):
        """
        True if tree contains the value
        O(logn)
        """
        return self._search_helper(self.root, value)

    def _search_helper(self, node, value):
        if not node:
            return False
        if node.val == value:
            return True
        if value < node.val:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)

    def count_range(self, left, right):
        """
        @return: number of items in range, O(nlogn)
        """
        return self.count_range_helper(self.root, left, right)

    def count_range_helper(self, node, left, right):
        if not node:
            return 0
        left_n = right_n = 0
        if node.val < left:
            right_n = self.count_range_helper(node.right, left, right)
        elif left <= node.val <= right:
            left_n = self.count_range_helper(node.left, left, right)
            right_n = self.count_range_helper(node.right, left, right)
        else:
            left_n = self.count_range_helper(node.left, left, right)

        return left_n + right_n + 1 if left <= node.val <= right else left_n + right_n


if __name__ == '__main__':
    array = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    bst = BST(array)
    bst.show()
    print(bst.count_range(3, 4))
