# سورت آرایه، بدون استفاده از تابع sot()



def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return



arr = [2, 5, 1, 0, 1.6, 9, 10]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("%.2f" % arr[i], end=" ")
