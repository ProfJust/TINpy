import math

# rueckgabewert = math.sqrt(25)
# print(rueckgabewert)

def circle_area(radius):
    area = math.pi * radius**2
    return area  # Rückgabewert


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
# main 
#rueckgabewert = circle_area(2.0)
#print(rueckgabewert)

print(absolute_value(-3))

print(is_divisible(6, 3))