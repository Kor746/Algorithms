
def insertion_sort(a):
	for i in range(1,len(a)):
		key = a[i]
		j = i - 1

		while (j >= 0) and (a[j] > key):
			a[j + 1] = a[j] 
			j -= 1

		a[j + 1] = key 

	return a;

def main():
	test_list = [1,4,2,3,10,6,12,13,4,3]

	print(insertion_sort(test_list))



if __name__ == '__main__':
	main()
