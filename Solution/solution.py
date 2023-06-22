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
#        for x in nums:
#            for y in nums:
#                if x == y:
#                    ##assuming we can't use the same element/index twice. This is not a provided assumption and nothing in the prompt contradicts this assumption.
#                    ##if we *were* allowed to use the same index twice, this if block would not exist.
#                    continue
#                if (x + y) == target:
#                    #complexity of list.index() is O(n)
#                    return [nums.index(x), nums.index(y)]

# Test case provided by LeetCode revealed there was a misunderstanding of the prompt. The provided test case was (3,3)
# The initial understanding of the prompt was that the test cases will not show the same element twice at different indexes.
# The reality is that the developer is not allowed to use the same index twice in order two get a sum, but the same number can be used at different indexes in the test case.
# The below solution will account for this new understanding of the problem, and the above solution will be left commented as future reference for anyone reading this Solution

        for indexOne in range(0,len(nums)): #range includes left operand and excludes right operand
            for indexTwo in range(0,len(nums)):
                if indexOne == indexTwo: #ignoring cases where indexes are the same
                    continue
                if nums[indexOne] + nums[indexTwo] == target:
                    return [indexOne,indexTwo]

        # The above solution uses the same kind of logic as the initial erroneous solution but takes into account the updated understanding of the prompt
        # Using indexes directly instead of elements allows referencing of duplicate elements existing at different indexes while ignoring cases when the indexes are the same
        # Solution has a nested iteration of the list, making this solution O(n^2)
        # Solution has been run against provided test cases in LeetCode and was accepted as a correct solution.
