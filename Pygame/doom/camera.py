from pygame import Vector2

class Camera:
    def __init__(self, bl_1: Vector2, tr_1: Vector2, bl_2: Vector2, tr_2: Vector2):
        self.bl_1 = bl_1
        self.tr_1 = tr_1
        self.bl_2 = bl_2
        self.tr_2 = tr_2


    def to_screen(self, coordinate: Vector2):
        scale_1, scale_2 = (self.tr_1 - self.bl_1) / 2, (self.tr_2 - self.bl_2) / 2
        offset = self.divide_vectors((coordinate - self.bl_1), scale_1)
        new = self.multiply_vectors(offset, scale_2) + self.bl_2
        return new
    

    def divide_vectors(self, v_1: Vector2, v_2: Vector2):
        return Vector2(v_1.x/ v_2.x, v_1.y / v_2.y)
    
    def multiply_vectors(self, v_1: Vector2, v_2: Vector2):
        return Vector2(v_1.x * v_2.x, v_1.y * v_2.y)