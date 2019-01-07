#Linked list is a connected sequence of elements.
class Node:
	"""Node is where data is stored in linked list. It holds data and pointer."""
	#Initialize a Node
	def __init__(self, data = None, next = None):
		"""Initialize a Node.
			Args:
			self: self object
			data: data in the node
			next: the next node
		Returns:
			None
		"""
		self.data = data
		self.next = next	
	def get_data(self):
		"""Get data from the node
		Args:
			self: the node itself
		Returns:
			Data in the node
		"""
		return self.data
	def get_next(self):
		"""Get the next node.
		Args:
			self: the node itself
		Returns:
			Next node
		"""
		return self.next

class LinkedList:
	"""Linked list is a connected sequence of elements."""
	def __init__(self):
		"""Initialize the linked list
		Args:
			self: the linked list itself
		Returns:
			None
		"""	
		self.head = None
	def add_node(self, data):
		"""Add data to the begining of linked list
		Args:
			self: linked list itself
			data: data to be inserted in the linked list
		Returns:
			None
		"""	
		if(self.head == None):
			self.head = Node(data)
		else:
			new_node = Node(data)
			new_node.next = self.head
			self.head = new_node

	def remove_node(self, data):
		"""Delete the first occurence of data forml linked list
		Args:
			self: the linked list itself
			data: data to be removed
		Returns:
			status: True/False (Success/ Fail)
		"""
		prev_node = None
		curr_node = self.head
		status = False
		while(curr_node is not None):
			if curr_node.get_data() == data:
				if prev_node:  #Checking if first node is to be removed
					prev_node.next = curr_node.next
					return True
				else:
					self.head = curr_node.next
					return True
			prev_node = curr_node
			curr_node = curr_node.next
		return status

	def print_list(self):
		"""Print the contents of linked list
		Args:
			self: linked list itself
		Returns:
			None
		"""
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next

my_list = LinkedList()
my_list.add_node(2)
my_list.add_node(5)
my_list.add_node(-6)
my_list.add_node(32)
my_list.print_list()
my_list.remove_node(5)
my_list.remove_node(6)
my_list.print_list()