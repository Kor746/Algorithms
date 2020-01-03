A = [31,41,59,26,41,58,35322,12,32,1]

for i in range(len(A)):
	smallest_ind = 0
	key = A[i]
	j = i + 1

	while j < len(A):
		if A[j] < key:
			key = A[j]
			smallest_ind = j

		j += 1

	if smallest_ind > 0:
		temp = A[i]
		A[i] = A[smallest_ind]
		A[smallest_ind] = temp


print(A)