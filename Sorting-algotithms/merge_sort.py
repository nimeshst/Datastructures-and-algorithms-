def merge_sort(arr):
	if len(arr) > 1:
		mid =  len(arr)//2

		L = arr[:mid]
		R = arr[mid:]

		merge_sort(L)
		merge_sort(R)

		merge_two_sorted_list(L, R, arr)


def merge_two_sorted_list(arr1, arr2, arr):

	i = j = k = 0

	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			arr[k] = arr1[i]
			i = i + 1
		else:
			arr[k] = arr2[j]
			j = j + 1
		k = k+1

	while i < len(arr1):
		arr[k] = arr1[i]
		i = i+1
		k = k + 1

	while j < len(arr2):
		arr[k] = arr2[j]
		j = j+1
		k = k+1
 

list1 = [66,44,33,77,88,87,90,123,2]

merge_sort(list1)
print(list1)

