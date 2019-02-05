#Bubble sort algorithm
#Worst Case time complexity is O(n2)
def bubble_sort(arr):
	def swap(i, j):
		arr[i], arr[j] = arr[j], arr[i]
	
	swapped = True
	l = len(arr)
	counter = 0

	while swapped:
		swapped = False
		for i in range(l-counter-1):
			if arr[i] > arr[i+1]:
				swap(i, i+1)
				swapped = True
		counter +=1
	return arr
my_array = [1, -1, 10, 2, 14, 12, 13, -6]
print(bubble_sort(my_array))
