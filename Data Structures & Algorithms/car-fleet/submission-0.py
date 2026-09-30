class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info = [[position[i], speed[i]] for i in range(len(position))]
        mono_pos = sorted(info, key=lambda x:x[0])

        fl = []
        for i, info in enumerate(mono_pos):
            time_to = (target - info[0]) / info[1]
            while fl and time_to >= (target - mono_pos[fl[-1]][0]) / mono_pos[fl[-1]][1]:
                fl.pop()

            fl.append(i)
        
        return len(fl)

        