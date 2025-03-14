from renderer import RenderWindow
from buffer import PixelBuffer


WIDTH, HEIGHT = 800, 600


def main():
    window = RenderWindow((WIDTH, HEIGHT), 30)

    buffer = PixelBuffer((WIDTH, HEIGHT))

    while window.running:
        window.process_events()

        buffer.randomize()
        window.render_from_buffer(buffer.array)


if __name__ == "__main__":
    main()