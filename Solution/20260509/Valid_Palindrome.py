# Version 1 Two pointer with space complexity O(n)
## 1. Build a filtered string containing only alphanumeric characters.
## 2. Convert all uppercase letters to lowercase.
## 3. Use two pointers to compare character from both ends.
## Time complexity: O(n), where n is the length of the input string.
## Space complexity: O(n), due to the additional filtered string.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = ""
        for c in s:
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
                valid_s += c.lower()
            elif c >= '0' and c <= '9':
                valid_s += c
        l = 0
        r = len(valid_s) - 1
        while l < r:
            if valid_s[l] != valid_s[r]:
                return False
            l+=1
            r-=1
        return True

# Version 2 Two pointer with space complexity O(1)
## 1. Use two pointers starting from both ends of the string.
## 2. Skip non-alphanumeric characters while moving the pointers.
## 3. Convert uppercase letters to lowercase before comparision.
## 4. Compare characters from both ends to check whether the string is a palindrome.
## Time complexity: O(n), where n is the length of the input string.
## Space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True