# insertion sort 

def insertion_sort(arr):

	# traverse through 1 to len(arr)
	for i in range(1,len(arr)):
		element_to_insert = arr[i]

		j = i - 1


		while j >= 0 and arr[j] > element_to_insert:
			# move the elements of the list one position ahead
			arr[j+1] = arr[j] 
			j = j-1

		# insert the elements to its correct position in the 
		# sorted list 
		arr[j+1] = element_to_insert
	print(arr)
			

test_arr = [10,22,34,24,56,54,2,99,42]
insertion_sort(test_arr)
