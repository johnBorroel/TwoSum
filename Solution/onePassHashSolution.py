#Starting with the script as provided by LeetCode which defines class Solution and member function twoSum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #This solution will make use of a hash table and whether the complement of the current element is already in the hash table
        #Hash Table lookup is O(1) and will not affect the time complexity of the Solution
        seenElements = dict()
        index = 0
        while index < len(nums):
            complement = target - nums[index]
            if (complement) in seenElements:
                return [seenElements[complement], index]
            else:
                seenElements[nums[index]] = index
                index += 1
        #Solution iterates through the list once, which is O(n) and only does lookups in hash table which is O(1), so the solution simplifies to O(n)
        #Solution has been run against provided test cases in LeetCode and was accepted as a correct solution.
