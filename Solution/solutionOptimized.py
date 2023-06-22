#Starting with the script as provided by LeetCode which defines class Solution and member function twoSum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #This solution will be faster than O(n^2) to satisfy the follow-up section of the prompt
        #Instead of nesting for loops per element for an O(n^2) iteration, we will search the list from both ends
        #in order to only loop through once in total, stopping when the indexes on either side match or pass each other
        leftIndex = 0
        rightIndex = len(nums)-1
        while leftIndex < rightIndex:
            if nums[leftIndex] + nums[rightIndex] == target: #get operation for single element is O(1)
                return [leftIndex, rightIndex]
            #increment/decrement
            leftIndex += 1
            rightIndex -= 1
        #The above solution iterates from both ends of the list and stops once the indexes meet or pass each other, whichever comes first
        #Since there is a guaranteed answer and the indexes work through the list together only once, the solution runs in O(n) time
