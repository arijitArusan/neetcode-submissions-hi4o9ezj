class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            hash1={}
            hash2={}
            for k,v in zip(s,t):
                if k in hash1:
                    hash1[k]+=1
                else:
                    hash1[k]=1
                if v in hash2:
                    hash2[v]+=1
                else:
                    hash2[v]=1
        if hash1==hash2:
            return True
        else:
            return False