# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertionsort(nums):
    count = 0
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
        	nums[j+1] = nums[j]
        	j -= 1
        	count += 1
        nums[j+1] = key
        print nums
    return count
    
a = [1, 3, 9, 8, 2, 7, 5]
def qsort(nums, start, end): 
	if start >= end:
		return 0
	r, count = partition(nums, start, end)
	count += qsort(nums, start, r-1)
	count += qsort(nums, r + 1, end)
	return count
def partition(nums, start, end):
	count = 0
	key = nums[end]
	i = start - 1
	for j in range(start, end):
		if nums[j] < key:
			i += 1
			nums[j], nums[i] = nums[i], nums[j]
			count += 1
	i += 1
	nums[i], nums[end] = nums[end], nums[i]
	count += 1
	return i, count
print qsort(a,0 , len(a) - 1)
print a