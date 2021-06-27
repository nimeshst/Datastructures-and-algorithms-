class Node:
	# contains node datastructure that for implementing 
	# linked list
	def __init__(self,data):
		self.data = data
		self.next = None # next pointer

	def __repr__(self):
		return self.data

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, data):
		self.data = data

	def set_next(self,next):
		self.next = next


class OrderLinkedList:
	# Ordered collection of nodes where each node
	# points to the next node 
	def __init__(self):
		self.head = None

	def add_node(self, item):
		current = self.head
		previous = None
		stop = False

		while current != None and not stop:
			if current.get_data() > item:
				stop = True
			else :
				previous = current
				current = current.get_next()

		if previous == None:
			node = Node(item)
			node.set_next(self.head)
			self.head = node

		else:
			node = Node(item)
			previous.set_next(node)
			node.set_next(current)


	def size(self):
		# returns the nummber of elements in the list
		current = self.head
		count = 0

		while current != None:
			current = current.get_next()
			count = count + 1

		return count


	def show(self):

		current = self.head
		list1 = []
		while current is not None:
			list1.append(current.get_data())
			current = current.get_next()

		return list1

	def search(self, item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.get_data() == item:
				found = True

			else:
				if current.get_data() > item:
					stop = True
				else:
					current = current.get_next()

		return found



	def remove(self, item):
		current = self.head
		found = False
		previous = None

		while not found:
			# iterate and set the current and previous
			# pointers accordingly 
			if current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()

		# check if the item is present in the list
		if previous == None:
			# iteam is present in the head
			self.head = current.get_next()

		else:
			# set the pointer of the previous to the next element of 
			# the current. 
			previous.set_next(current.get_next())




mylist = OrderLinkedList()

mylist.add_node(31)
mylist.add_node(77)
mylist.add_node(17)
mylist.add_node(93)
mylist.add_node(26)
mylist.add_node(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
print(mylist.search(54))
mylist.remove(54)
print(mylist.search(54))
print(mylist.size())
mylist.remove(93)
print(mylist.size())

print(mylist.show())