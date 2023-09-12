
from math import pi
class Circle:

    def __init__(self,radious :int ,color : str ,x_position : int ,y_position : int ):
        self.radious = radious
        self.color =  color
        self.position= (x_position,y_position)

    def get_position(self):
        return self.position

    def change_color(self,new_color ):
        self._color=new_color

    def __str__(self):
        my_str=f"this is circle with radious {self._radious} color {self._color}"
        return my_str
#added on 30/7/2023
    @classmethod
    def from_string(cls,my_str):
        return cls(1,"red",4,5)  #return object of circle

    @staticmethod
    def is_date_valid( date_as_string ):
        day, month, year = map(lambda val: int(val), date_as_string.split('-'))
        return dat <= 31 and month <= 12 and year <= 3999

    @staticmethod
    def sum(a,b):
        return a+b

# end of addition
    def get_area(self):
        return pi*self.radious**2

    def move_position(self,x:int,y:int):
        _x,_y=self.position
        self.position= (_x+x,_y+y)

my_circle=Circle(4,"red",6,7)
a=my_circle.get_position()
my_circle.change_color("green")
print("a",a)
print(my_circle)
a = str(my_circle)
print(a)

#copy to new folder oop\main.py
from  circle  import Circle
moshe= Circle(4,"red",1,1 )



#on 31/7/2023
a=Circle.from_string("adsd")
print('a', a)

a=  Circle.from_string("assd")
print(a)


b=Circle.is_date_valid("1-1-1987")