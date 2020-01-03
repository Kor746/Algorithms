
a, b = 0, 0

#O(nLogn) solution
def mss(aList,low,high):
	if low == high:
		return aList[low]
	mid = (low + high) // 2
	left_sum = mss(aList,low,mid)
	right_sum = mss(aList,mid + 1,high)
	# print(mid)
	cross_sum = max_crossing(aList,low,mid,high)
	# print(max(left_sum,right_sum,cross_sum))
	# print(left_sum)
	# print(right_sum)
	global a, b
	if cross_sum > left_sum and cross_sum > right_sum:
		a = low
		b = high
	else:
		if left_sum < right_sum:
			a = mid + 1
			b = high
		else:
			a = low
			b = mid
		

	return max(left_sum,right_sum,cross_sum)

def max_crossing(aList,low,mid,high):
	
	left_sum = 0
	s = 0
	for i in range(mid,low - 1,-1):
		s += aList[i]
		if s > left_sum: 
			left_sum = s
	right_sum = 0
	s = 0
	for i in range(mid+1, high + 1):
		s += aList[i]
		if s > right_sum:
			right_sum = s

	return left_sum + right_sum

# def mno():



def main():
	# list_of_nums = [4,3,-10,3,-1,2,0,-3,5,7,-4,-8,-10,4,7,-30,-2,-6,4,7]

	list_of_nums = [2,4,5,-7,3,-6,1,4]
	# list_of_nums = [4,3,-10,3,-1,2,0,-3,5,7,-4,-8,-10,4,7,-30,-2,-6,4,7]


	max_seg = mss(list_of_nums,0,len(list_of_nums)-1)
	global a, b
	print("a",a,"b",b)
	list_of_nums2 = list_of_nums
	for i in range(a,b+1):
		print(list_of_nums[i],)
		list_of_nums2[i] = -99 
		

	
	max_seg = mss(list_of_nums2,0,len(list_of_nums2)-1)
	print(list_of_nums2)
	for i in range(a,b+1):
		# list_of_nums2[i] = -99 
		print(list_of_nums2[i],)

	print(max_seg)



if __name__ == '__main__':
	main()