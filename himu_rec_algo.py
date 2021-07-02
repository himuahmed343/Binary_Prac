
def binary_search(arr, low, high, x):

	if high >= low:
		mid = low + (high - low) // 2


		if arr[mid] == x:
			return mid


		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		elif arr[mid] < x:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1


arr = ['A', 'C', 'E', 'B', 'F', 'L', 'M', 'N', 'D', 'I']
x = 'N'


result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", result, '& Value is', arr[result])
else:
	print("Element is not present in array")
