#wap to create a class point and calculate the distance b/w two points objects in 2d
from math import sqrt
class point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def distance(self,user):
        d=sqrt(pow((user.x-self.x),2)+pow((user.y-self.y),2))
        return d
    def display(self):
        print(f"the distance is:-{self.distance()}")

