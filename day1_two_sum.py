#Given a list of integers and a target number, 
# return the indices of the two numbers that add up to the target. 
# Assume there's exactly one solution, 
# and you can't use the same element twice

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]

print(two_sum([2,7,11,15],9))


