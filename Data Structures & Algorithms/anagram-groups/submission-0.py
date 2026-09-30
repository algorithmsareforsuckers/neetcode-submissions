from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Immediate idea: hash containing counter : list[str], return the values
        patterns = {}
        for s in strs:
            alph = "".join(sorted(s))
            patterns[alph] = patterns.get(alph, []) + [s]
        
        rets = []
        for pat in patterns.values():
            rets.append(pat)
        
        return rets
        