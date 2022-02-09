from cmath import pi
from dataclasses import dataclass
import click

@dataclass
class Vector:
    x: float = 0
    y: float = 0

@dataclass(init=True, frozen=True)
class Shape(object):

    _id: int

    @classmethod
    def create(cls, id: int) -> "Shape":
        return Shape(id)
    
    def __repr__(self) -> str:
        return f"""
        {self.name} (id: {self.id})
        """
    
    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def position(self) -> Vector: 
        raise NotImplementedError

    @property
    def perimeter(self) -> float: 
        raise NotImplementedError
    
    @property
    def area(self) -> float: 
        raise NotImplementedError

    @property
    def volume(self) -> float: 
        raise NotImplementedError
    
    @property
    def id(self) -> int:
        return self._id

@dataclass(init=True, frozen=True)
class Point(Shape):

    _position: Vector

    @classmethod
    def create(cls, id: int) -> "Point":
        x = click.prompt("Input x coordinate", type=float)
        y = click.prompt("Input y coordinate", type=float)
        position = Vector(x, y)

        return Point(id, position)
    
    def __repr__(self) -> str:
        return f"""
        {self.name} (id: {self.id})
        Position: {self.position}
        """

    @property
    def position(self) -> Vector:
        return self._position

@dataclass(init=True, frozen=True)
class Circle(Point):
    _radius: float

    @classmethod
    def create(cls, id: int) -> "Circle":
        x = click.prompt("Input x coordinate", type=float)
        y = click.prompt("Input y coordinate", type=float)
        r = click.prompt("Input radius", type=click.FloatRange(min=0,max_open=True))
        position = Vector(x, y)

        return Circle(id, position, r)
    
    def __repr__(self) -> str:
        return f"""
        {self.name} (id: {self.id})
        Position: {self.position}
        Radius: {self._radius}
        Perimeter: {self.perimeter}
        Area: {self.area}
        """

    @property
    def perimeter(self) -> float:
        return self._radius * pi * 2
    
    @property
    def area(self) -> float:
        return pi * (self._radius ** 2)

@dataclass(init=True, frozen=True)
class Cylinder(Circle):
    _height: float

    @classmethod
    def create(cls, id: int) -> "Cylinder":
        x = click.prompt("Input x coordinate", type=float)
        y = click.prompt("Input y coordinate", type=float)
        r = click.prompt("Input radius", type=click.FloatRange(min=0,max_open=True))
        h = click.prompt("Input height", type=click.FloatRange(min=0,max_open=True))
        position = Vector(x, y)

        return Cylinder(id, position, r, h)
    
    def __repr__(self) -> str:
        return f"""
        {self.name} (id: {self.id})
        Position: {self.position}
        Radius: {self._radius}
        Height: {self._height}
        Perimeter: {self.perimeter}
        Area: {self.area}
        Volume: {self.volume}
        """

    @property
    def perimeter(self) -> float:
        return super().perimeter * 2
    
    @property
    def area(self) -> float:
        return super().area + super().perimeter * self._height
    
    @property
    def volume(self) -> float:
        return super().area * self._height

@dataclass(init=True, frozen=True)
class Rectangle(Point):
    _width: float
    _height: float

    @classmethod
    def create(cls, id: int) -> "Rectangle":
        x = click.prompt("Input x coordinate", type=float)
        y = click.prompt("Input y coordinate", type=float)
        w = click.prompt("Input width", type=click.FloatRange(min=0,max_open=True))
        h = click.prompt("Input height", type=click.FloatRange(min=0,max_open=True))
        position = Vector(x, y)

        return Rectangle(id, position, w, h)
    
    def __repr__(self) -> str:
        return f"""
        {self.name} (id: {self.id})
        Position: {self.position}
        Width: {self._width}
        Height: {self._height}
        Perimeter: {self.perimeter}
        Area: {self.area}
        """

    @property
    def perimeter(self) -> float:
        return (self._width + self._height) * 2
    
    @property
    def area(self) -> float:
        return self._width * self._height

@dataclass(init=True, frozen=True)
class Square(Point):
    _size: float

    @classmethod
    def create(cls, id: int) -> "Square":
        x = click.prompt("Input x coordinate", type=float)
        y = click.prompt("Input y coordinate", type=float)
        s = click.prompt("Input size", type=click.FloatRange(min=0,max_open=True))
        position = Vector(x, y)

        return Square(id, position, s)
    
    def __repr__(self) -> str:
        return f"""
        {self.name} (id: {self.id})
        Position: {self.position}
        Size: {self._size}
        Perimeter: {self.perimeter}
        Area: {self.area}
        """

    @property
    def perimeter(self) -> float:
        return self._size * 4
    
    @property
    def area(self) -> float:
        return self._size ** 2

@dataclass(init=True, frozen=True)
class Cube(Square):

    @classmethod
    def create(cls, id: int) -> "Cube":
        x = click.prompt("Input x coordinate", type=float)
        y = click.prompt("Input y coordinate", type=float)
        s = click.prompt("Input size", type=click.FloatRange(min=0,max_open=True))
        position = Vector(x, y)

        return Cube(id, position, s)

    def __repr__(self) -> str:
        return f"""
        {self.name} (id: {self.id})
        Position: {self.position}
        Size: {self._size}
        Perimeter: {self.perimeter}
        Area: {self.area}
        Volume: {self.volume}
        """

    @property
    def perimeter(self) -> float:
        return super().perimeter * 3
    
    @property
    def area(self) -> float:
        return super().area * 8
    
    @property
    def volume(self) -> float:
        return super().area * self._size

SHAPES_MAP = {
    "shape": Shape,
    "point": Point,
    "circle": Circle,
    "cylinder": Cylinder,
    "rectangle": Rectangle,
    "square": Square,
    "cube": Cube,
}