class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)



q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print(q.dequeue())
print('size - ',q.size())
q.enqueue('44')
q.enqueue(99)
q.enqueue(36)
print(q.dequeue())
print('size -',q.size())
