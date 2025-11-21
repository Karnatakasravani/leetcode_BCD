class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        # for i in range(len(nums)):
        #     dic[nums[i]] = i
        for num in range(len(nums)):
            dif =(target - nums[num])
            if dif in dic:
                return [num,dic[dif]]
            dic[nums[num]] = num 

        # return dic
