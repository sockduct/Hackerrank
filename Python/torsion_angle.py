import math

class PointIterator:
    def __init__(self, point):
        self._point = point
        self._index = 0

    def __next__(self):
        if self._index < 3:
            if self._index == 0:
                res = self._point.x
            elif self._index == 1:
                res = self._point.y
            else:
                res = self._point.z

            self._index += 1
            return res

        raise StopIteration


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return PointIterator(self)

    def __repr__(self):
        return f'<x={self.x}, y={self.y}, z={self.z}>'

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __sub__(self, other):
        return Point(other.x - self.x, other.y - self.y, other.z - self.z)

    def abs(self):
        return (self.x**2 + self.y**2 + self.z**2)**(0.5)

    def dot(self, other):
        return sum(self_i * other_i for self_i, other_i in zip(self, other))

    def cross(self, other):
        return Point(self.y * other.z - self.z * other.y,
                     self.z * other.x - self.x * other.z,
                     self.x * other.y - self.y * other.x)


def main():
    points = []
    for _ in range(4):
        point = Point(*map(int, input().split()))
        points.append(point)

    a, b, c, d = points
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y)/(x.abs() * y.abs()))

    print(f'{math.degrees(angle):.2f}')


if __name__ == '__main__':
    main()
