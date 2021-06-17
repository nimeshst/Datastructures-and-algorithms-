# bubble sort 

def bubble_sort(arr):

	# traverese the through all array elements

	for i in range(len(arr)-1):
		swapped = False
		# last i elements are already sorted 
		for j in range(0, len(arr)-i-1):
			# compare the adjacent two elemets 
			if arr[j] > arr[j+1]:

				# swap the elements
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		if swapped == False:
			# no swap happened so the list is already 
			# sorted and thus terminate the loop
			break

	print(arr)
			

test_arr = [10,22,34,24,56,54,2]
bubble_sort(test_arr)
