#Starting with the script as provided by LeetCode which defines class Solution and member function twoSum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #First solution will be simple and aim for O(n^2) to start
        #Iterating through the list and iterating again per element to find pairs will guarantee we find the solution in O(n^2) time
        #since we may assume there is exactly one solution.
        for x in nums:
            for y in nums:
                if x == y:
                    #assuming we can't use the same element/index twice. This is not a provided assumption and nothing in the prompt contradicts this assumption.
                    #if we *were* allowed to use the same index twice, this if block would not exist.
                    continue
                if (x + y) == target:
                    #complexity of list.index() is O(n)
                    return [nums.index(x), nums.index(y)]
