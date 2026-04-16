# Day 4: Maximum Subarray Sum of Size K (Sliding Window)
#
# Given an array of integers and a number k, find the maximum sum
# of any contiguous subarray of size k.
#
# This pattern is everywhere in AI/ML engineering — think moving
# averages over sensor data, rolling metrics in monitoring systems,
# or windowed feature extraction in time series models.
#
# Example:
#   Input:  nums = [2, 1, 5, 1, 3, 2], k = 3
#   Output: 9
#   Explanation: Subarray [5, 1, 3] has the maximum sum of 9
#
# Another example:
#   Input:  nums = [2, 3, 4, 1, 5], k = 2
#   Output: 7
#   Explanation: Subarray [3, 4] has the maximum sum of 7
#
# Constraints:
#   - 1 <= k <= len(nums)
#   - The array will have at least one element
#
# Hint: You don't need to recalculate the entire sum each time.
#       What if you just "slid" the window by removing the leftmost
#       element and adding the next one on the right?
#
# Write your solution below:

def max_subarray_sum(nums, k):
    window_sum  = sum(nums[:k])
    max_sum   = window_sum
    
    for i in range(len(nums)-k):
        window_sum = window_sum - nums[i] + nums[i+k]
        max_sum = max(max_sum, window_sum)
    return max_sum



# Test cases
print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3))  # Expected: 9
print(max_subarray_sum([2, 3, 4, 1, 5], 2))      # Expected: 7
print(max_subarray_sum([1, 1, 1, 1, 1], 3))      # Expected: 3
print(max_subarray_sum([5], 1))                    # Expected: 5
