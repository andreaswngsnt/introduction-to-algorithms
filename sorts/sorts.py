import math

# Insertion Sort
print("INSERTION SORT")
list_a = [5, 2, 4, 6, 1, 3]
def insertion_sort(array):

	# Go through all element in the list
	for i in range(0, len(array) - 1):
		# If the next element is smaller than the current element...
		if (array[i + 1] < array[i]):

			# Go through all the elements before...
			for j in range(0, i + 1):
				# If there is a previous element that is just bigger than the next element,
				if (array[j] > array[i + 1]):
					# Save the element to a variable
					moved_element = array[i + 1]
					# Remove the current element from its previous position
					del array[i + 1]
					# Put the element in the correct position
					array.insert(j, moved_element)

	return array

print("Unsorted List")
print(list_a)
print("Sorted List")
print(insertion_sort(list_a))

print("\n")

# Bubble Sort
print("BUBBLE SORT")
list_b = [5, 2, 4, 6, 1, 3]

def bubble_sort(array):
	# Keep looping until the list is sorted completely
	sorted = False
	while not sorted:
		sorted = True
		# For each element in the list...
		for i in range(0, len(array) - 1):

			# Compare the current element with the next element
			if (array[i] > array[i + 1]):
				# Switch the element if it's out of order
				big_num = array[i]
				small_num = array[i + 1]
				array[i] = small_num
				array[i + 1] = big_num
				sorted = False

	return array

print("Unsorted List")
print(list_b)
print("Sorted List")
print(bubble_sort(list_b))

print("\n")

# Selection Sort
print("SELECTION SORT")
list_c = [5, 2, 4, 6, 1, 3]

def selection_sort(array):

	# Loop as many as the number of element
	for i in range(0, len(array)):
		# Assume the loop number is the index of the smallest element
		smallest_element_index = i
		smallest_element = array[i]

		# Go through the assumed smallest element to the last element
		for j in range(i, len(array)):
			# Find the smallest element
			if array[j] < smallest_element:
				smallest_element = array[j]
				smallest_element_index = j

		# Move the smallest element to the loop number index
		del array[smallest_element_index]
		array.insert(i, smallest_element)

	return array

print("Unsorted List")
print(list_c)
print("Sorted List")
print(selection_sort(list_c))