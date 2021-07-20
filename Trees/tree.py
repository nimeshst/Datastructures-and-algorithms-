class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left =  None
		self.right = None


class BinaryTree():
	def __init__(self, root):
		self.root = Node(root)


tree = BinaryTree(6)
tree.root.left = Node(4)
tree.root.right = Node(7)
tree.root.right.left = Node(3)
tree.root.right.right = Node(10)
tree.root.left.right = Node(44)
tree.root.left.rleft = Node(12)

# 			|-12
# 	|-4--
# 	|		|-44
# 6 -
# 	| 	|-3
# 	|-7--
# 			|-10
	
