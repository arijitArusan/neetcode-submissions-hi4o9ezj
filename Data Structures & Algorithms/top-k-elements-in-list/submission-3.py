class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Frequency map
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Step 2: Buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Traverse from highest frequency
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
