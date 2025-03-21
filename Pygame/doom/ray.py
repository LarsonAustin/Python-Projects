from pygame import Vector2
import math


MAX_DEPTH = 9


class Ray:
    def __init__(self, angle, origin: Vector2 = Vector2(0, 0)):
        self.vector = Vector2(math.cos(angle), math.sin(angle))
        self.origin = origin

    def cast_x(self, grid):
        x_ray = self.vector * (1 / (self.vector.y - 0.0000001))

        if self.vector.y > 0:
            x_offset = x_ray * (1 - (self.origin.y % 1))
            for i in range(MAX_DEPTH):
                cast = self.origin + x_offset + (i * x_ray)
                cast.y += 0.1
                try:
                    #print(int(cast.x), int(cast.y))
                    g = grid[int(cast.x)][int(cast.y)]
                    if g:
                        return x_offset + (i * x_ray)
                except:
                    pass
        else:
            x_offset = x_ray * (self.origin.y % 1)
            x_offset = -x_offset
            for i in range(MAX_DEPTH):
                cast = self.origin + x_offset + (i * x_ray)
                cast.y -= 0.1
                try:
                    #print(int(cast.x), int(cast.y))
                    g = grid[int(cast.x)][int(cast.y)]
                    if g:
                        return x_offset + (i * x_ray)
                except:
                    pass
        return Vector2(100, 100)


    def cast_y(self, grid):
        y_ray = self.vector * (1 / (self.vector.x - 0.0000001))

        if self.vector.x > 0:
            y_offset = y_ray * (1 - (self.origin.x % 1))
            for i in range(MAX_DEPTH):
                cast = self.origin + y_offset + (i * y_ray)
                cast.x += 0.1
                try:
                    #print(int(cast.y), int(cast.y))
                    g = grid[int(cast.y)][int(cast.x)]
                    if g:
                        return y_offset + (i * y_ray)
                except:
                    pass
        else:
            y_offset = y_ray * (self.origin.x % 1)
            y_offset = -y_offset
            for i in range(MAX_DEPTH):
                cast = self.origin + y_offset + (i * y_ray)
                cast.x -= 0.1
                try:
                    #print(int(cast.y), int(cast.y))
                    g = grid[int(cast.y)][int(cast.x)]
                    if g:
                        return y_offset + (i * y_ray)
                except:
                    pass
        return Vector2(100, 100)


    def cast(self, grid):
        x_ray = self.cast_x(grid)
        y_ray = self.cast_y(grid)

        if x_ray.magnitude() > y_ray.magnitude():
            return y_ray
        return x_ray