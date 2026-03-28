# Write your solution here
def create_tuple(x: int, y: int, z: int):
    t = x + y + z
    if x < y and x < z:
        if y > z:
            point = (x,y,t)
        else:
            point = (x,z,t)
    elif y < x and y < z:
        if x > z:
            point = (y,x,t)
        else:
            point = (y,z,t)
    else:
        #z is less
        if x > y:
            point = (z,x,t)
        else:
            point = (z,y,t)
    return point


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
