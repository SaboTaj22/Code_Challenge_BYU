# Given a non-empty array of
# integers
# nums, every
# element
# appears
# twice except for one.Find that single one.
#
# You
# must
# implement
# a
# solution
# with a linear runtime complexity and use only constant extra space.
#
# Example
# 1:
#
# Input: nums = [2, 2, 1]
# Output: 1
# Example
# 2:
#
# Input: nums = [4, 1, 2, 1, 2]
# Output: 4
# Example
# 3:
#
# Input: nums = [1]
# Output: 1
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each
# element in the
# array
# appears
# twice except for one element which appears only once.

class Solution(object): # this solution uses the XOR operation
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= num
        return result

class Solution(object):
    def singleNumber(self, nums):

        dictionary = {}  # initialize an empty dictionary

        for num in nums:  # iterate over the numbers in the array
            dictionary[num] = dictionary.get(num, 0) + 1
            # use the .get method to find the value of a num and increment count of num each time it appears.

        for single_val, element_val in dictionary.items():  # check through values after incrementation
            if element_val == 1:  # if the value occurs only once
                return single_val  # return the value that has only occured once