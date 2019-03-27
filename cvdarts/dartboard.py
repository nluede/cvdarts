import math
"""

     ----------------- X --------------->
 |     
 |                    20
 |                %%%    %%%
 |           %%%              %%%
   
 Y       %%%                      %%%
   
 |      %%%                         %%%
 |  11                o------ 0° ----  6
 |      %%%           |             %%%
 |                    |
 |      %%%           |            %%%
 |                    |
 |         %%%       90 °       %%%
 |                    |
\|/              %%%     %%%
 v                    3
"""


class Board(object):

    def __init__(self):
        self.fields = [
            BoardField(score=20, angle=270),
            BoardField(score=1, angle=288),
            BoardField(score=18, angle=306),
            BoardField(score=4, angle=324),
            BoardField(score=13, angle=342),
            BoardField(score=6, angle=0),
            BoardField(score=10, angle=18),
            BoardField(score=15, angle=36),
            BoardField(score=2, angle=54),
            BoardField(score=17, angle=72),
            BoardField(score=3, angle=90),
            BoardField(score=19, angle=108),
            BoardField(score=7, angle=126),
            BoardField(score=16, angle=144),
            BoardField(score=8, angle=162),
            BoardField(score=11, angle=180),
            BoardField(score=14, angle=198),
            BoardField(score=9, angle=216),
            BoardField(score=12, angle=234),
            BoardField(score=5, angle=252)
        ]

    def print(self):
        for f in self.fields:
            print(f.score)

            x, y = f.get_coordinates_top_left()

            print("aNGLE: " + str(f.left_angle()))
            print("X: " + str(x) + ", Y: " + str(y))
            print("")


class BoardField(object):
    def __init__(self, score, angle):
        self.score = score
        self.angle = angle

    def left_angle(self):
        result = self.angle - 8
        if result < 0:
            result = result + 360
        return result

    def get_coordinates_top_left(self):
        angle = self.left_angle()
        return math.cos(math.radians(angle)), math.sin(math.radians(angle))

