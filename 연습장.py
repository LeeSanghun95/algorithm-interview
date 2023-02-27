
nums = [3,2,4]
target = 6
List = [int]



def twoSum(nums: List, target: int) -> List:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return print([i,j])       

twoSum(nums, target)

