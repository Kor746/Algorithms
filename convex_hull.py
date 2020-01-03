import random 
# random.seed(2)
# list_of_points = [(x,y) for x in range(random.randint(1,5),random.randint(6,10)*2) for y in range(random.randint(1,5),random.randint(6,10)*2)]

def get_random_points(up_bound):
	list_of_points = []
	for i in range(0, random.randint(1,up_bound)):
		list_of_points.append((random.randint(5,20),random.randint(5,20)))
	return list_of_points


def get_leftmost_point(list_of_points):
	leftmost_point = list_of_points[0]
	for i in range(1,len(list_of_points)):
		if leftmost_point[0] > list_of_points[i][0]:
			leftmost_point = list_of_points[i]
	return leftmost_point

# def sort_list_by_slope(list_of_points):
# 	for i in range(1,len(list_of_points)):
# 		print(list_of_points[i], list_of_points[i-1])
# 		slope_of_line = abs(list_of_points[i][1] - list_of_points[i-1][1]) / abs(list_of_points[i][0] - list_of_points[i-1][0])
# 		print(slope_of_line)

def get_convexhull(list_of_random_points,n):
	# Need at least 3 points to get orientation
	if n < 3: return;

	list_of_hulls = []
	poh = get_leftmost_point(list_of_random_points)
	#insert leftmost point to hull list
		
	for i in range(0,n):
		list_of_hulls.append(poh)
		q = list_of_random_points[i]
		for j in range(0,n):
			if i != j:
				r = list_of_random_points[j]
				# print(poh,q,r)
				orientation = get_orientation(poh,q,r)
				# print(orientation)
				if orientation < 0:
					q = r
				# print(q)
		poh = q
		if q == list_of_hulls[0]:
			break;
	return list_of_hulls


#Calculate differences of slopes to get direction, left is positive, right is negative
def get_orientation(a,b,p):
	return (p[0] - b[0]) * (a[1] - b[1]) - (p[1] - b[1]) * (a[0] - b[0])

# function is_on_left(a, b, p){
# 	d =  (p[0] - b[0]) * (a[1] - b[1]) - (p[1] - b[1]) * (a[0] - b[0]);
#   if(d > 0) return true;
#   return false;
# }

def main():
	list_of_random_points = get_random_points(50)
	length_of_points = len(list_of_random_points)
	print(list_of_random_points)
	result = get_convexhull(list_of_random_points,length_of_points)
	print(result)
if __name__ == '__main__':
	main()