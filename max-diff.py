'''
We consider an array A[1...n]. Write a function that returns:
Max_{i=1..n, j <= i} (A[i] - A[j])
	 
(the largest difference in the array between a value and another value with a smaller index)
'''

def max_diff(a):
	d = 0
	y = a[0]
	for x in a[1:]:
		d = max(d, x - y)
		y = min(y, x)
	return d

# test output
print(max_diff([2, 1, 9])) # 8
print(max_diff([1, 2, 9])) # 8
print(max_diff([9, 1, 2])) # 1
print(max_diff([1, 9, 2])) # 8
print(max_diff([2, 9, 1])) # 7
print(max_diff([9, 2, 1])) # 0

print(max_diff([2, 7, 1, 9])) # 8
print(max_diff([2, 7, 1, 5])) # 5
