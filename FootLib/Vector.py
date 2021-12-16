class Vector:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        ''' Addition '''
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        ''' Substraction '''
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        ''' Multiplision '''
        if isinstance(other, int):
            # произведение вектора на число
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            # скалярное произведение
            return self.x * other.x + self.y * other.y

    def __str__(self):
        return f'<Vector({self.x}, {self.y})>'
