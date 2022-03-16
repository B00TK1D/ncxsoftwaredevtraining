if __name__ == '__main__':
    print("Advent of Code - Day 5")

    # save day 5 input as list
    list_of_lists=[]
    with open("input.txt","r") as f:
        lines = f.read()
        list_of_lists = lines.splitlines()
    print(list_of_lists)

    def cordinate(obj):
        # Convert the co-ordinates from string format to int format
        return tuple(map(int, obj.split(',')))

def draw_horizontal_line(grid, y, x, x1):
    intersections = 0
    # Range is inclusive of both ends i.e., min to max
    for i in range(min(x, x1), max(x, x1) + 1):
        grid[(i, y)] += 1
        
        # Once we find a intersection, we increment the intersections counter
        if grid[(i, y)] == 2:
            intersections += 1
    return intersections

def draw_vertical_line(grid, x, y, y1):
    intersections = 0
    # Range is inclusive of both ends i.e., min to max
    for i in range(min(y, y1), max(y, y1) + 1):
        grid[(x, i)] += 1

        # Once we find a intersection, we increment the intersections counter
        if grid[(x, i)] == 2:
            intersections += 1
    return intersections








