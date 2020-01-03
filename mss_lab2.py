
# list_of_nums = [2,4,5,-7,3,-6,1,4]
list_of_nums = [4,3,-10,3,-1,2,0,-3,5,7,-4,-8,-10,4,7,-30,-2,-6,4,7]
# list_of_nums = [5,5,5,-10,-10,-10,7,7,7]

# O(nlogn)
# Daniel Lee
list_of_nums2 = [1,2,3,4,5,6]
list_segment_elements = []
def mss(i): 
	list_segment_elements.append(list_of_nums[i])
	if i == 0:
		return list_of_nums[i] 

	return max(list_of_nums[i], list_of_nums[i] + mss(i-1))
max_segment = []
def mno(a,b):
	if len(a) == 0:
		return 0;
	result = 0
	besti = 0

	for i in range(1,len(a)):
		if a[i] > b[besti]:
			max_segment.append(a[i])
			result += 1
			besti = i 
	return result + 1;


def main():
	# list_of_segment_sums = []
	if len(list_of_nums) != 1:
		for i in range(1,len(list_of_nums),1):
			segment_sum = mss(i)
			print(list_segment_elements)
			print(segment_sum)
			list_segment_elements.clear()
		# maximum_segment_sum = max(list_of_segment_sums)
	# x = mno(list_of_nums,list_of_nums2)
	print(max_segment)
		
if __name__ == '__main__':
	main()