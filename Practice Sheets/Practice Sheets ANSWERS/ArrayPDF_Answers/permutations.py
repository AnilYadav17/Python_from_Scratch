'''46. Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]'''



nums = [1,2,3]

if len(nums) == 1:
	return [nums]

result = []

for i in range(len(nums)):
	current = nums[i]
	remaining = nums[:i] + nums[i+1:]
	print(current,remaining)
