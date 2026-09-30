class CountSquares:

    def __init__(self):
        self.pcount = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pcount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        x,y = point[0], point[1]

        for a,b in self.points:
            if (abs(x-a) != abs(y-b)) or x == a or y == b:
                continue
            
            res += self.pcount[(x, b)] * self.pcount[(a, y)]
        return res