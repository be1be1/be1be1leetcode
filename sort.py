def bubblesort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1, i, -1):
			if arr[j] < arr[j-1]:
				arr = swap(arr, j-1, j)
	return arr
	

def selectionsort(arr):
	for i in range(len(arr)):
		minidx = i
		for j in range(i+1, len(arr), 1):
			if arr[j] < arr[minidx]:
				minidx = j
		arr = swap(arr, i, minidx)
		
	return arr
	

def insertionsort(arr):
	for i in range(1, len(arr)):
		if arr[i] < arr[i-1]:
			j = i-1
			target = arr[i]
			while j > -1 and target < arr[j]:
				arr[j+1] = arr[j]
				j -= 1
			arr[j+1] = target
	return arr
		

def quicksort(arr, left, right):
	if left < right:
		pivot = arr[left]
		i = left
		j = right
		
		while i < j:
			while arr[j] >= pivot and i < j:
				j -= 1
			while arr[i] <= pivot and i < j:
				i += 1
			arr = swap(arr, i, j)
			
		arr[left] = arr[i]
		arr[i] = pivot
		
		quicksort(arr, left, i-1)
		quicksort(arr, i+1, right)
		return arr

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr
	
print(bubblesort([4,3,7,1,3,8,2]))
print(selectionsort([4,3,7,1,3,8,2]))
print(insertionsort([4,3,7,1,3,8,2]))
print(quicksort([4,3,7,1,3,8,2], 0, 6))
	
			