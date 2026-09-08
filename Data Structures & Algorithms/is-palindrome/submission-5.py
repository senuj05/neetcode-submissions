class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the string
        clean = []
        for i in s:
            if i.isalnum():
                clean.append(i.lower())

        # intialize two pointers
        left, right = 0, len(clean)-1;
        
        while left < right:
            if clean[left] != clean[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        