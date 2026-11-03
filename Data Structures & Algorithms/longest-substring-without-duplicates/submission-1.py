class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        current_substring = []
        for char in s:
            try:
                current_substring = current_substring[current_substring.index(char)+1:]
            except ValueError:
                pass
            current_substring.append(char)
            if len(current_substring) > result:
                result = len(current_substring)

        return result

        