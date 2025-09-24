class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_arr = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            diff = target - num
            if diff in sum_arr:
                return [sum_arr[diff],i]
            sum_arr[num] = i
            i+=1