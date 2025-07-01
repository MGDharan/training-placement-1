# Filename: polygon_area.py
def calculate_polygon_area(coordinates):
    """Calculates the area of a polygon given its coordinates."""
    area = 0.0
    n = len(coordinates)
    for i in range(n):
        j = (i + 1) % n
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]
    return abs(area) / 2.0