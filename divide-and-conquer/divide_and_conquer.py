import math

# MERGE SORT
print("MERGE SORT")
list_d = [5, 2, 4, 6, 1, 3]

def merge_sort(array):
	sorted_array = []
	mid_array_index = math.floor(len(array) / 2)
	array_a = array[:mid_array_index]
	array_b = array[mid_array_index:]

	if len(array_a) > 1:
		array_a = merge_sort(array_a)
	if len(array_b) > 1:
		array_b = merge_sort(array_b)

	i = 0
	j = 0

	while i < len(array_a) and j < len(array_b):
		if array_a[i] < array_b[j]:
			sorted_array.append(array_a[i])
			i += 1
		else:
			sorted_array.append(array_b[j])
			j += 1
	
	while i < len(array_a):
		sorted_array.append(array_a[i])
		i += 1

	while j < len(array_b):
		sorted_array.append(array_b[j])
		j += 1

	return sorted_array

print("Unsorted List")
print(list_d)
print("Sorted List")
print(merge_sort(list_d))

print('\n')

#
# MAXIMUM SUBARRAY
#

print("MAXIMUM SUBARRAY")
dailyPrices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
print("Daily Prices, starting at day 1")
print(dailyPrices)

# Put the changes of daily price in an array
array = []
for i in range(1, len(dailyPrices)):
	priceChange = dailyPrices[i] - dailyPrices[i - 1]
	array.append(priceChange)

print("Daily Price Change, starting at day 2")
print(array)

#
# Linear Approach
#
potential_max_subarray_sums = []
potential_max_subarray_sum_start_indexes = []
potential_max_subarray_sum_end_indexes = []
for i in range(0, len(array)):
	if i > 0:
		extended_sum_element = array[i] + potential_max_subarray_sums[i - 1]
		if extended_sum_element > array[i]:
			potential_max_subarray_sums.append(extended_sum_element)
			potential_max_subarray_sum_start_indexes.append(potential_max_subarray_sum_start_indexes[i - 1])
			potential_max_subarray_sum_end_indexes.append(i)
			continue
	potential_max_subarray_sums.append(array[i])
	potential_max_subarray_sum_start_indexes.append(i)
	potential_max_subarray_sum_end_indexes.append(i)

max_subarray_sum = potential_max_subarray_sums[0]
max_subarray_sum_start_index = potential_max_subarray_sum_start_indexes[0]
max_subarray_sum_end_index = potential_max_subarray_sum_end_indexes[0]
for i in range(0, len(potential_max_subarray_sums)):
	if potential_max_subarray_sums[i] > max_subarray_sum:
		max_subarray_sum = potential_max_subarray_sums[i]
		max_subarray_sum_start_index = potential_max_subarray_sum_start_indexes[i]
		max_subarray_sum_end_index = potential_max_subarray_sum_end_indexes[i]

print()
print("Max profit: ${}".format(max_subarray_sum))
print("When to buy: Day {}".format(max_subarray_sum_start_index + 1))
print("When to sell: Day {}".format(max_subarray_sum_end_index + 2))