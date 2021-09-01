class Node:
    def __init__(self,value,left = None,right = None):
        self.left = left
        self.right = right
        self.value = value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value
    
    def set_right(self,right):
        self.right = right

    def set_left(self,left):
        self.left = left
    
    def set_value(self,value):
        self.value = value


    def add_node(self,node):
        if node.value < self.value:
            if self.left:
                self.left.add_node(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.add_node(node)
            else:
                self.right = node


    def search(self,value):
        if self.value == value:
            return print(f"Found the node: {self}")
        if value>self.value:
            if self.right:
                self.right.search(value)
            else:
                return print("Value doesn't exist in this tree")
        else: 
            if self.left:
                self.left.search(value)
            else:
                return print("Value doesn't exist in this tree")


    #display is a recursive function to display a binary tree,copied from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self):
        lines, *_ = self.display_aux()
        for line in lines:
            print(line)

    def display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display_aux()
        right, m, q, y = self.right.display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

root = Node(8)
node_10 = Node(10)
node_3 = Node(3)
node_14 = Node(14)
node_13 = Node(13)
node_6 = Node(6)
node_1 = Node(1)
node_7 = Node(7)
node_4 = Node(4)
root.add_node(node_10)
root.add_node(node_3)
root.add_node(node_14)
root.add_node(node_13)
root.add_node(node_6)
root.add_node(node_1)
root.add_node(node_7)
root.add_node(node_4)
root.search(8)
root.display()