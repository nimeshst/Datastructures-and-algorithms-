class Node:

	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

	def get_data(self):
		return self.data

	def set_data(self,data):
		self.data = data

	def get_next(self):
		return self.next

	def get_prev(self):
		return self.prev

	def set_next(self,next):
		self.next = next

	def set_prev(self, prev):
		self.prev = prev



class DoublyLinkedList():

	def __init__(self):
		self.head = None


	def add_node_at_start(self, item):

		if self.head is None:
			node = Node(item)
			self.head = node
			
			return

		node = Node(item)
		node.set_next(self.head)
		self.head.set_prev(node)
		self.head = node


	def add_node_at_end(self, item):
		if self.head == None:
			node = Node(item)
			self.head = node

			return

		current = self.head
		while current.get_next() != None:
			current = current.get_next()

		node = Node(item)
		current.set_next(node)
		node.set_prev(current)


	def remove(self, item):
		pass
		"""
		if self.head == None:
			print('empty list')
			return

		if self.head.get_data() == item:
			# item present at the start
			self.head = self.head.get_next()
			self.head.set_prev(None)
			return

		current = self.head
		found = False
		while not found:
			if current.get_data() == item:
				found = True
			current = current.get_data()

		if current.get_next() is not None:
			current.get_prev().set_next(current.get_next())
			current.get_next().set_prev(current.get_prev())
		else : 
			if current.get_data() == item:
				current.get_prev().set_next(None)

			else:
				print('item not find')
				return
"""

	def size(self):
		current = self.head
		count = 0

		while current != None:
			current = current.get_next()
			count = count + 1

		return count

	def search():
		pass
	
	def reverse(self):
		pass


mylist = DoublyLinkedList()

mylist.add_node_at_start(77)
mylist.add_node_at_start(710)	



print(mylist.size())
mylist.add_node_at_start(89)
mylist.remove(710)
print(mylist.size())
