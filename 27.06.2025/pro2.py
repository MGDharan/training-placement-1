class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def evaluate(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return int(node.val)
    lval = evaluate(node.left)
    rval = evaluate(node.right)
    if node.val == '+':
        return lval + rval
    if node.val == '-':
        return lval - rval
    if node.val == '*':
        return lval * rval
    if node.val == '/':
        return lval / rval

# Example tree: ((3+2)*(4-1))
root = Node('*')
root.left = Node('+')
root.right = Node('-')
root.left.left = Node('3')
root.left.right = Node('2')
root.right.left = Node('4')
root.right.right = Node('1')

print(evaluate(root))
