class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1=Point(10,20)
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2 =Point(1,5)
point2.x=1
print(point2.x)
point =Point(10,20)
print(point.x)