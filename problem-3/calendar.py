from typing import Optional

class Node():
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        # insert right child
        if node.start >= self.end:
            if not self.right_child: 
                self.right_child = node
                return True
            return self.right_child.insert(node)
        # insert left child
        elif node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)

        return False

class Calendar():
    def __init__(self):
        self.root: Node = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        return self.root.insert(node=Node(start, end))

calendar = Calendar()
print(calendar.book(5, 10)) # -> Expect True
print(calendar.book(8, 13)) # -> Expect False
print(calendar.book(10, 15)) # -> Expect True
