class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        valold=None
        maxsize=0
        substring=[]
        for i,k in enumerate(s):
            if i==0:
                valold=k
                substring.append(valold)
                maxsize=len(substring)
                continue
            if k in substring:
                index = substring.index(k)
                substring = substring[index + 1:]
                valold=k
                substring.append(valold)
                if maxsize<len(substring):
                    maxsize=len(substring)
            else:
                valold=k
                substring.append(valold)
                if maxsize<len(substring):
                    maxsize=len(substring)
        return maxsize