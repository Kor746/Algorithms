import csv
import numpy
import random

list_of_arrivals = [1,2,3]
list_of_departures = [3,4,5]
# with open('start1.csv', 'r') as f:
# 	for i in f:
# 		list_of_arrivals.append(float(i.strip('\n')))

# # print(list_of_arrivals)

# with open('finish1.csv', 'r') as f:
# 	for i in f:
# 		list_of_departures.append(float(i.strip('\n')))
# print(list_of_departures)

gates = 0

list_of_gates = []
# maxn = 1
for i in range(0,len(list_of_arrivals)):
	n = 1
	for j in range(0,len(list_of_departures)):
		if i != j:
			if list_of_arrivals[j] > list_of_arrivals[i] and list_of_arrivals[j] < list_of_departures[i]:
				n += 1
	list_of_gates.append(n)
# print(list_of_gates)
print(max(list_of_gates))

# def allow_lateness(list_of_arrivals,list_of_departures):
# 	gates = 0

# 	list_of_gates = []
# 	# maxn = 1
# 	for i in range(0,len(list_of_arrivals)):
# 		n = 0
# 		for j in range(0,len(list_of_departures)):
# 			if i != j:
# 				# print(list_of_arrivals[i])
# 				if list_of_arrivals[j] >= list_of_arrivals[i] and list_of_arrivals[j] <= list_of_departures[i]:
# 					n += 1
# 		list_of_gates.append(n)
# 	return list_of_gates


# random_uniform_delay = numpy.random.uniform(low=0.0,high=1.0,size=None)
# # print(list_of_arrivals)
# # print(list_of_departures)
# for i in range(0, len(list_of_arrivals)-1):
# 	random_aircraft_index = random.randint(0,len(list_of_arrivals)-1)
# 	list_of_arrivals[random_aircraft_index] = list_of_arrivals[random_aircraft_index] + random_uniform_delay
# 	list_of_departures[random_aircraft_index] = list_of_departures[random_aircraft_index] + random_uniform_delay
# # print(list_of_arrivals)
# # print(list_of_departures)
# list_of_gates = allow_lateness(list_of_arrivals,list_of_departures)

# # random_fraction_of_aircrafts  = random(0, len(list_of_arrivals))
# print(max(list_of_gates))
	# if n > maxn:
	# 	maxn = n
	# if min((x,y), < j:
		# gates += 1

#print(list_of_gates)
#print(sum(list_of_gates))
# print(max(list_of_gates))

