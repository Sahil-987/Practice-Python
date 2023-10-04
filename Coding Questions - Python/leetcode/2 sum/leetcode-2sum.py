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
## Iska better version ye h, ki dictionary banana aur residual search saath me karo

class Solution:
    def twoSum(self, nums, target):

        # ## Method-1 | pahle dict banao aur baad me residual search karo
        # #create dict
        # value_index_dict = {} # keys = value of the list element, values = index of the list element
        # for i in range(len(nums)):
        #     value_index_dict[nums[i]] = i

        # for j in range(len(nums)):
        #     residual = target - nums[j]
        #     if residual in value_index_dict and j != value_index_dict[residual]:
        #         return [j,value_index_dict[residual]]


        ## Method-2 | dict banao aur residual search SAATH me karo

        value_index_dict = {} # keys = value of the list element, values = index of the list element

        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in value_index_dict:
                return [i, value_index_dict[residual]]
            value_index_dict[nums[i]] = i
            


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    print(Solution().twoSum(nums, target))


    ## my test case | not unique solution
    
    nums = [2,7,11,15,3,6]
    target = 9

    print(Solution().twoSum(nums, target))