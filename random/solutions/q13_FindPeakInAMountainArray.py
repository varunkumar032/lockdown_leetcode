# Let's call an array arr a mountain if the following properties hold:

# 1. arr.length >= 3
# 2. There exists some i with 0 < i < arr.length - 1 such that:
# 	a. arr[0] < arr[1] < ... arr[i-1] < arr[i]
# 	b. arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# Example 1:
# Input: arr = [0,1,0]
# Output: 1

# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1

# Example 4:
# Input: arr = [3,4,5,1]
# Output: 2

# Example 5:
# Input: arr = [24,69,100,99,79,78,67,36,26,19]
# Output: 2

def peakIndexInMountainArray(arr):
	n = len(arr)
	left = 0
	right = n - 1
	while left < right:
		mid = left + (right-left)//2
		if arr[mid] > arr[mid+1]:
			right = mid
		else:
			left = mid + 1
	return left
