#Selection Sort divides the list/array into two parts
#the sublists of the items already sorted
#the sublets remaining to be sorted
def selection_sort(arr):
	def swap(i, j):
		arr[i], arr[j] = arr[j], arr[i]

	position, counter = 0, 0

	for i in range(len(arr)):
		minimum = arr[i]
		for j in range(i+1, len(arr)):
			if minimum > arr[j]:
				position = j
				minimum = arr[position]
		swap(counter, position)
		counter += 1
	return arr

my_arr = [1, -1, 12, 5, 1, 2, 0]
print(selection_sort(my_arr))