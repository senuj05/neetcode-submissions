class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False

        dic_s ={}
        for char in s:
            dic_s[char]= dic_s.get(char, 0)+1

        dic_t={}
        for char in t:
            dic_t[char]=dic_t.get(char,0)+1

        return dic_s ==dic_t
