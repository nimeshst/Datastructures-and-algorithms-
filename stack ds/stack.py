class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		# return the last element of the list
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)



s = Stack()
s.push(10)
print(s.peek())
s.push(99)
s.push(56)
print(s.peek())
s.push(97)
s.push(54)
print(s.pop())

s.push(215)
s.push(778)
s.push(8.4)
print(s.pop())
print(s.pop())
print('size -',s.size())

