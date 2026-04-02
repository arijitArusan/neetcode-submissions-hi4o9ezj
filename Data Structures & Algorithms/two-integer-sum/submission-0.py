class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        i=0
        for i,val in enumerate(nums):
            k=target-val
            if k in seen:
                return[seen[target-val],i]
            seen[val]=i
            i+=1