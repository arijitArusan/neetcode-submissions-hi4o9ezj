import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        i=0
        k=[]
        while i<len(nums):
            a=nums[0:i]
            b=nums[i+1:]
            if a==[]:
                k.append(math.prod(b))
            elif b==[]:
                k.append(math.prod(a))
            else:
                k.append(math.prod(a)*(math.prod(b)))
            i+=1
        return k