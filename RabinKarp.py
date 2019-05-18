class RabinKarp:
	def __init__(self, text, sizeWord):
		self.text = text
		self.hash = 0
		self.sizeWord = sizeWord

		for i in range(0, sizeWord-1):
			#ord maps the character to a number
			#subtract out the ASCII value of "a" to start the indexing at zero
			self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))

		#start index of current window
		self.window_start = 0
		#end of index window
		self.window_end = sizeWord

	def window_text(self):
		return self.text[self.window_start:self.window_end]
