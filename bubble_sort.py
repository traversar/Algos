def bubble_sort(array):
	for item in range(len(array)):
		for j in range(0, (len(array) - item - 1)):
			if array[j] > array[j + 1]:
				(array[j], array[j + 1]) = (array[j + 1], array[j])
