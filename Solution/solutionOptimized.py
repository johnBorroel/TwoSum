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
#        leftIndex = 0
#        rightIndex = len(nums)-1
#        while leftIndex < rightIndex:
#            if nums[leftIndex] + nums[rightIndex] == target: #get operation for single element is O(1)
#                return [leftIndex, rightIndex]
#            #increment/decrement
#            leftIndex += 1
#            rightIndex -= 1
#        #The above solution iterates from both ends of the list and stops once the indexes meet or pass each other, whichever comes first
#        #Since there is a guaranteed answer and the indexes work through the list together only once, the solution runs in O(n) time

# Test case provided by LeetCode revealed there was a misunderstanding of the prompt. The provided test case was (3,3)
# The initial understanding of the prompt was that the test cases will not show the same element twice at different indexes.
# The reality is that the developer is not allowed to use the same index twice in order two get a sum, but the same number can be used at different indexes in the test case.
# The above solution also mistakenly updates left and right indexes by the same amount each time which doesn't account for all pair combinations.
# The below solution will account for this new understanding of the problem, and the above solution will be left commented as future reference for anyone reading this Solution

        #Expanding on the above erroneous solution, this solution will sort the list first using the built in sort which runs in O(n*Log(n)) time
        #It should be noted that using a sort like Radix sort or Counting sort which are O(n) could make this solution even faster in *certain* situations
        numsSorted = sorted(nums)
        sortedLeftIndex = 0
        sortedRightIndex = len(numsSorted)-1
        while sortedLeftIndex < sortedRightIndex:
            if numsSorted[sortedLeftIndex] + numsSorted[sortedRightIndex] == target:
                originalLeftIndex = nums.index(numsSorted[sortedLeftIndex]) #O(n)
                if numsSorted[sortedLeftIndex] == numsSorted[sortedRightIndex]:
                    originalRightIndex = nums[originalLeftIndex+1:].index(numsSorted[sortedRightIndex]) + originalLeftIndex + 1 #cutting out everything before and including the first instance found by index method to avoid it giving the same index twice in the event of duplicate elements at different indexes, then accounting for the cut-off indexes
                else:
                    originalRightIndex = nums.index(numsSorted[sortedRightIndex])
                return [originalLeftIndex, originalRightIndex]
            elif numsSorted[sortedLeftIndex] + numsSorted[sortedRightIndex] < target:
                sortedLeftIndex += 1
            elif numsSorted[sortedLeftIndex] + numsSorted[sortedRightIndex] > target:
                sortedRightIndex -= 1
        #The above solution uses an O(n*Log(n)) sort, which makes the remainder of the solution simplify to O(n*Log(n)). As mentioned in previous comments, in the correct situation, a sort with O(n) complexity can be used which would lower the time complexity further.
        #This solution was tested against the test cases provided by LeetCode and accepted as a correct solution.
