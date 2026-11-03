# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         result = 0
#         current_substring = []
#         for char in s:
#             try:
#                 current_substring = current_substring[current_substring.index(char)+1:]
#             except ValueError:
#                 pass
#             current_substring.append(char)
#             if len(current_substring) > result:
#                 result = len(current_substring)

#         return result

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res