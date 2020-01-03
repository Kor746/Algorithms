# amount = 5 
# coins = [1,2,5]

# mem = {5 : true, 2 + 2 + 1: true,
# 1 + 1 + 1 + 2: true, 1 + 1 + 1 + 1 : true}
# len(mem)

# we set up a while loop going from the highest to lowest
# we recurse

class Diamond():
	def create_diamond(self, n):
		if n & 1 == 1:
			self.print_diamond(0, n, n >> 1)
		else:
			return;
	def print_diamond(self, left, right, mid):
		if left < right:
			if left <= mid:
				print((" " * (mid - left)) + ("*" * ((left << 1) + 1)))
				self.print_diamond(left + 1, right, mid)
				if left != 0:
					print((" " * (mid - left + 1)) + ("*" * ((left - 1 << 1) + 1)))

n = 35
diamond = Diamond()
diamond.create_diamond(n)