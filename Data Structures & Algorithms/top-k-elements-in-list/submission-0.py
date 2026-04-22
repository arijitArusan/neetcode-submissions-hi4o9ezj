class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap={}
        for f in nums:
            if f in hashmap:
                hashmap[f]+=1
            else:
                hashmap[f]=1
        sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        first_n = list(sorted_dict)[:k] 
        return first_n
