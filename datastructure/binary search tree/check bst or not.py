class newNode: 

	# Construct to create a new node 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

# Returns true if given tree is BST. 
def isBst(root):
	c



# Driver Code 
if __name__ == '__main__': 
	root = newNode(50) 
	root.left = newNode(30) 
	root.right = newNode(70) 
	root.right.left = newNode(49) 
	root.right.right = newNode(80) 
	#root.right.left.left = newNode(40) 
	if (isBst(root)): 
		print("Is BST") 
	else: 
		print("Not a BST") 