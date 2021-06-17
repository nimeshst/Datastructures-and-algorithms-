# selection sort
def selection_sort(arr):

	for i in range(0,len(arr)):

		min_index = i

		j = i + 1
		# find the minimum element in the 
		# remaining unsorted list

		for j in range (i+1, len(arr)):

			if arr[min_index] > arr[j]:
				min_index = j

		arr[min_index], arr[i] = arr[i], arr[min_index]

	print(arr)


# a sorting algorithm is said to be sorted if the recurring
# elements appear in the input same order as they did in output 

def stable_selection_sort(arr):

	for i in range(len(arr)):
		min_index = i

		j = i + 1

		for j in range (i+1, len(arr)):

			if arr[min_index] > arr[j]:
				min_index = j

		key = arr[min_index]

		while min_index > i :
			arr[min_index] = arr[min_index-1]

			min_index = min_index-1
		arr[i] = key

	print(arr)

test_arr = [10,22,34,24,56,54,2,99,42]
selection_sort(test_arr)

test_arr = [10,22,34,24,56,54,2,99,42]
print(test_arr)
stable_selection_sort(test_arr)
