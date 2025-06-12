class Solution:
    def judgeCircle(self, moves: str) -> bool:
        convertion = {'U':-1, 'L': -1, 'R': 1, 'D': 1}
        x, y = 0, 0
        for i in moves:
            if i=='U' or i=='D':
                y+=convertion[i]
            elif i=='L' or i=='R':
                x+=convertion[i]

        return True if x==0 and y==0 else False