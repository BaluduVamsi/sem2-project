def distance(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(3)) ** 0.5

def nearest(points):
    nearest_neighbors = []
    
    for x in points:
        min_distance = 100000
        nearest_point = None
        
        for y in points:
            if y != x:
                dist = distance(x, y)
                if dist < min_distance:
                    min_distance = dist
                    nearest_point = y
        
        nearest_neighbors.append((x, nearest_point))
    
    return nearest_neighbors

points = [list(map(int, input("enter 10 points each 3d point sep by space").split())) for _ in range(10)]
result = nearest(points)
print(result)