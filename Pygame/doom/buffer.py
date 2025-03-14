import numpy as np

class PixelBuffer:
    def __init__(self, buffer_size):
        self.array = np.zeros((buffer_size[1], buffer_size[0], 3), dtype=np.uint8)

    def randomize(self):
        self.array[:, :, :] = np.random.randint(0, 256, self.array.shape, dtype=np.uint8)