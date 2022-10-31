# Python3 program to check if there is a subset
# with sum divisible by m.

# Returns true if there is a subset
# of arr[] with sum divisible by m
def helper(N, nums, sum, idx, m):

	# if we reach last index
	if(idx == N):
	
		# and if the sum mod m is zero
		if(sum and sum%m == 0):

			# return
			return True
	
		return False

	# 2 choices - to pick or to not pick
	picked = helper(N, nums, sum+nums[idx], idx+1,m)
	notPicked = helper(N, nums, sum,		 idx+1, m)

	return picked or notPicked

def modularSum(arr, n, m):
	return helper(n, arr, 0, 0, m)

# Driver code
arr = [1, 7]
n = len(arr)
m = 5

print("YES") if modularSum(arr, n, m) else print("NO")

# This code is contributed by shinjanpatra.
