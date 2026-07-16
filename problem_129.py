#kadane's problem
# Input:
# [-2,1,-3,4,-1,2,1,-5,4]

# Output:
# 6

# Explanation:
# Subarray = [4,-1,2,1]
# Sum = 6

def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


nums = [-2,1,-3,4,-1,-2,1,-5,4]
print(maxSubArray(nums))