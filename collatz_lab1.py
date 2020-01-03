import matplotlib.pyplot as plt
import sys

n = int(sys.argv[1])

def collatz_loop(n):
	list_of_indexes = []
	list_of_iterations = []
	list_of_prev_values = []

	for index in range(1,n+1):

		x = index
		i = 0
		# list_of_finite_prev_vals = { range(1,1000):''}
		# print(list_of_finite_prev_vals)
		# for key,val in list_of_finite_prev_vals.items():
		# 	print(key)
		while x != 1 and x not in list_of_prev_values:
			# print(x)
			if x in list_of_prev_values:
				break;
			if x % 2 == 0:
				x =  x // 2
			else:
				x = x * 3 + 1

			list_of_prev_values.append(x)
			i += 1
		print(str(index) + " : " + str(i))
		# list_of_prev_values.append(index)
		list_of_indexes.append(index)
		list_of_iterations.append(i)
	print(list_of_prev_values)
	print(list_of_iterations)
	# plt.plot(list_of_indexes,list_of_iterations)
	# plt.xlabel('Index n')
	# plt.ylabel('Number of iterations')
	# plt.show()

collatz_loop(n)
