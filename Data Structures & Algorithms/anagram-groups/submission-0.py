class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(x)) for x in strs]
        annagrams = {sorted_strs[0]: [strs[0]]}
        sorted_strs = sorted_strs[1:]
        for i, sorted_str in enumerate(sorted_strs):
            if sorted_str in annagrams:
                annagrams[sorted_str].append(strs[i+1])
            else:
                annagrams[sorted_str] = [strs[i+1]]
        return list(annagrams.values())