class newNode: 

	# Construct to create a new node 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

# Returns true if given tree is BST. 
def isBst(root,min = -1000,max=1000):
	min = -1000
	max = 1000
	if root == None:
		return True
	if root>min and root < max:
		return isBst(root.left,min,root.data) and isBst(root.right,root.data,max)

	else:
		return False



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