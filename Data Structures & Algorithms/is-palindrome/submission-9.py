class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right :

            # left side - move left pointer forward, till its point to an alphanumeric char
            while left < right and not s[left].isalnum():
                left += 1
            #  right side : same
            while left < right and not s[right].isalnum():
                right -=1
            # compare in lower case
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
