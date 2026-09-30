class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True

        num = len(hand) // groupSize

        std = sorted(hand)
        groups = [[] for _ in range(num)]

        i = 1
        k,c = 0,0
        for i in range(len(hand)):
            if not groups[k]: 
                groups[k].append(std[i])
                continue

            if std[i] == groups[k][-1]:
                k += 1
                if k >= num: return False
                groups[k].append(std[i])
                continue

            k = c
            if std[i] != groups[k][-1] + 1:
                return False
            
            # i = curr[-1] + 1
            groups[k].append(std[i])
            if len(groups[k]) == groupSize:
                c += 1
                k += 1
                
        return True


