import math


class SynError(Exception):
    def __init__(self, message="Invalid syntax"):
        super().__init__(message)


def get_player_pos() -> tuple:
    taken = 0
    while (True):
        try:
            inputs = input(
                    "Enter new coordinates as floats in format '"
                    "x,y,z':  "
                    )
            lst = inputs.split(",")
            if len(lst) != 3:
                raise SynError()
            for i in range(len(lst)):
                lst[i] = float(lst[i])
            taken += 1
            x, y, z = lst
            tup = (x, y, z)
            return tup

        except ValueError as e:
            print(f"Error on parameter '{lst[i]}':  {e}")
        except SynError as e:
            print(e)


def main():
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    tup1 = get_player_pos()
    x1, y1, z1 = tup1
    print("Got a first tuple:  ", tup1)
    print(f"It includes:  X={x1}, Y={y1}, Z={z1}")
    dist1 = math.sqrt(x1 * x1 + y1 * y1 + z1 * z1)
    print(f"Distance to center:  {dist1:.4f}")
    print("\nGet a second set of coordinates")
    tup2 = get_player_pos()
    x2, y2, z2 = tup2
    dist2 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    print(f"Distance between the 2 sets of coordinates:  {dist2:.4f}")


main()
