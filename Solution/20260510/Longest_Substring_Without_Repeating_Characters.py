# Version 1 Brute Force
## List substring start from i and sequentially check whether there is duplicate character.
### if there is duplicate character => invalid
### if there isn't duplicate character => valid, update length of longest substring
## Time complexity: O(n^2), where n is the length of the string
## Space complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res

# Version 2 Sliding Window
## We can keep one window that always has unique characters
## we expand the window by moving the right pointer
## if we ever see a repeated character, we shrink the window from the left until the duplicate is removed.
## This way, the window always represents a valid substring, and we track its maximum size.
## Time complexity: O(n), where n is the length of the string
### Explanation: Although there is a nested while loop, each character is added to and removed from the set at most once.
## Space complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res