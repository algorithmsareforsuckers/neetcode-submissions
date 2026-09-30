class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # just need to make a dict where the keys are a canonical form of the anagram, unmutable. I will sort them

        std = defaultdict(list)

        for word in strs:
            canonical = "".join(sorted(word))
            print(canonical)
            std[canonical].append(word)
        
        return list(std.values())

