class Ladder():

	# { 3: 22, 5: 8, 11: 26, 20: 29 }
	def __init__(self, head, tail) -> None:
		self.start = head
		self.end = tail

	def __eq__(self, other):
		return self.start == other.end and self.start == other.end
