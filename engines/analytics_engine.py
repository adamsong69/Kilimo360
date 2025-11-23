def shoelace_area(coords):
    n = len(coords)
    if n < 3:
        return 0
    a = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i+1)%n]
        a += x1*y2 - x2*y1
    return abs(a) / 2

def perimeter(coords):
    import math
    per = 0
    for i in range(len(coords)):
        x1,y1 = coords[i]
        x2,y2 = coords[(i+1)%len(coords)]
        per += math.hypot(x2-x1, y2-y1)
    return per
