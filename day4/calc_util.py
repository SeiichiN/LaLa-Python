import math

def get_triangle_area(bottom, height):
    return float(bottom) * float(height) / 2.0

def get_rectangle_area(width, height):
    return float(width) * float(height)

def get_circle_area(radius):
    return (float(radius) ** 2) * math.pi

if __name__ == '__main__':
    circle = get_circle_area(3)
    print(circle)
    
