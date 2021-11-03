# Postorder traversal
# Left ->Right -> Root
from node import Node
def PostorderTraversal(root):
    res = []
    if root:
        res = PostorderTraversal(root.left)
        res = res + PostorderTraversal(root.right)
        res.append(root.data)
    return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(PostorderTraversal(root))