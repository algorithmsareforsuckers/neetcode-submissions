class Solution:

    def encode(self, strs: List[str]) -> str:
        end = ""
        for s in strs:
            if not s:
                end += "0" + ","
                continue
            end += str(len(s)) + ","
        end += "|"

        for s in strs:
            end += s
        
        return end

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        curr = ""
        lens = []
        init = True
        i = 0
        while init:
            if s[i] == "|":
                init = False
            else:
                num = ""
                while s[i] != ",":
                    num += s[i]
                    i += 1

                lens.append(int(num))
            i += 1
        
        for l in lens:
            bound = i + l
            while i < bound:
                curr = curr + s[i]
                i = i + 1
            res.append(curr)
            curr = ""
        
        return res


