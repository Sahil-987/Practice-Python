"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Note :
exactly one pair
return index of the elements not values


Solutions:

1- Brute Force
2- Create Hash Table | key = value of the element, value = index of the element

"""


## My solution | Hint liya h youtubers se

class Solution:
    def twoSum(self, nums, target):

        #create dict
        value_index_dict = {} # keys = value of the list element, values = index of the list element
        for i in range(len(nums)):
            value_index_dict[nums[i]] = i

        for j in range(len(nums)):
            residual = target - nums[j]
            if residual in value_index_dict and j != value_index_dict[residual]:
                return [j,value_index_dict[residual]]
            


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    print(Solution().twoSum(nums, target))