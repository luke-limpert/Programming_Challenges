#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #will allow us to skip duplicate solutions
        nums.sort()

        length, result = len(nums), []

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #multiply by negative one
            #this allows for the sum of the other two numbers
            #to negate the value of the target
            target = nums[i] * -1

            #indexer
            start, end = i + 1, length - 1

            while start < end:
                #append list if the numbers negate to 0
                if nums[start] + nums[end] == target:
                    result.append([nums[i], nums[start], nums[end]])
                    start = start + 1
                    #skip similar elements to make sure we do not duplicate
                    #this is why we .sort() in the beginning
                    while start < end and nums[start] == nums[start - 1]:
                        start = start + 1

                #numbers did not negate - continue
                elif nums[start] + nums[end] < target:
                    start = start + 1
                else:
                    end = end - 1
        return result