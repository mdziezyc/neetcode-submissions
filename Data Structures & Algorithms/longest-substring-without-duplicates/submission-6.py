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
        last_idx_for_char = {}
        left_idx = 0
        result = 0

        for right_idx in range(len(s)):
            if s[right_idx] in last_idx_for_char:
                left_idx = max(last_idx_for_char[s[right_idx]] + 1, left_idx)
            last_idx_for_char[s[right_idx]] = right_idx
            result = max(result, right_idx - left_idx + 1)
        return result