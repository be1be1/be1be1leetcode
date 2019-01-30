class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        substr = ''

        for char in s:
            if char not in substr:
                substr += char
                ans = max(ans, len(substr))
            else:
                substr = substr[substr.index(char) + 1:] + char

        return ans
