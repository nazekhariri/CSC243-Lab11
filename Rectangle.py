from Point import Point
class Rectangle:
    def __init__(self,p,q):
        assert type(p) is Point and type (q) is Point and p.x<= q.x and p.y <=q.y, "Bad input!"
        self.p = p
        self.q = q
        
    def __str__(self):
        return f"p={self.p}, q={self.q}"
    
    def get_width(self):
        return self.q.x - self.p.x
    
    def get_height(self):
        return self.q.y - self.q.y 
    
    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())
    
    def area(self):
        return self.get_width() * self.get_height()
    
    def contains(self, pt):
        assert type(pt) is Point, "Bad input!"
        return self.p.x <= pt.x <= self.q.x and self.p.y <= pt.y <= self.q.y
