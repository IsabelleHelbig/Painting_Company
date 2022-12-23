# Assignment3 - CPRG216
#
# The application calculates the total interior surface area to be painted, the amount of paint needed, and the total cost of the job,
# including supplies and labour.  The executives remind you that a typical room in a house has four walls, with opposite walls being
# equal.  Walls can be rectangular or square in shape.  Some rooms, however, might have fewer than four walls (not all walls will be
# painted) or more than four (odd shaped rooms).
#
# Inputs:
#   number of rooms
#   Length, width and height
#   number of doors and window
#
# Processing Calculations:
#   Rectangular Area
#   Square Area
#   Custom Area
#
# Output:
#   Area to be painted in square feet
#   Amount of gallons to paint
#   Approximate cost of paint
#
# Author Andy Lee, Isabelle Helbig, Ekom Uffort
# Version 2022-11-18

import math
GallonssPerDollar = 42.00
squareFeetPerGallon = 350.00
profitMargin = 0.30
LabourCostPerFeetSquared = 0.15


def computeRoomArea(roomNum):
    print(f"Room: {roomNum}")

    print("""
Select the shape of the room:
1–Rectangular
2–Square
3-Custom (more or less than 4 walls, all square or rectangles)

Option: """, end=''
          )
    roomShape = int(input())

    if roomShape == 1:
        area = computeRectangleWallsArea()
    elif roomShape == 2:
        area = computeSquareWallsArea()
    elif roomShape == 3:
        area = computeCustomWallsArea()
    else:
        print("Invalid input, Enter a number between 1-3 (inclusive)")
        quit()
    gallons = computeGallons(area)
    cost = computePaintPrice(area)
    print(f"\nFor Room: {roomNum}, Area to be painted: {area:0.1f} square ft, and will require {gallons:0.2f} gallons to paint. The paint will cost approximately: ${cost:0.2f}\n")
    return area


def computeRectangleWallsArea():
    l = float(input("Enter the length for room length in feet: "))
    w = float(input("Enter the width for room width in feet: "))
    h = float(input("Enter the height for room height in feet: "))
    frontArea = computeRectangleArea(l, h)
    sideArea = computeRectangleArea(h, w)
    surfaceArea = (2*sideArea) + (2*frontArea)

    winDoorArea = computeWindowsDoorsArea()
    return (surfaceArea - winDoorArea)


def computeRectangleArea(x, h):
    # Returns base * height
    return (x*h)


def computeSquareWallsArea():
    l = float(input("Enter one side length of the room in feet: "))
    h = float(input("Enter the height of the room in feet: "))

    surArea = computeSquareArea(l, h)
    winDoorArea = computeWindowsDoorsArea()

    return (4*surArea - winDoorArea)


def computeSquareArea(l, h):
    return l*h


def computeWindowsDoorsArea():
    area = 0
    numWinOrDoors = int(input("How many windows and doors are in the room? "))
    for i in range(1, 1+numWinOrDoors):
        l = float(
            input(f"Enter the window/door length for window/door {i} length in feet: "))
        w = float(
            input(f"Enter the window/door width for window/door {i} width in feet: "))

        area += l*w
    return area


def computeCustomWallsArea():
    area = 0
    numWalls = int(input("How many walls are there in the room? "))
    # Area of each wall
    for i in range(1, 1 + numWalls):
        l = float(input(f"What is the length for wall {i} length in feet: "))
        h = float(input(f"What is the height for wall {i} height in feet: "))
        area += l*h
    winDoorArea = computeWindowsDoorsArea()
    # Return net surface area
    return area - winDoorArea


def computeGallons(area):
    # 350 square feet per gallon of paint
    return (area / squareFeetPerGallon)


def computePaintPrice(area):
    # 42 dollars per gallon of paint
    cost = computeGallons(area)*GallonssPerDollar

    answer = (round(cost, 2))
    return answer


def main():
    print("Welcome to Shiny Paint Company for indoor painting!")

    numRoom = int(input("How many rooms do you want to paint: "))
    print("Thank you!")

    netCost, netArea = 0, 0,
    for i in range(1, 1 + numRoom):

        netArea += computeRoomArea(i)

# 350 square feet per gallon of paint

    netGallons = math.ceil(netArea/squareFeetPerGallon)
# Cost per gallon of paint
    netCost += netGallons*GallonssPerDollar
# Labour cost per feet squared
    netCost += LabourCostPerFeetSquared*netArea
# Profit margin (30 percent)
    netCost += netCost*profitMargin
    print(f"Total area to be painted is {netArea:0.1f} square ft and will require {netGallons} gallon(s) to paint.\nThe total customer estimate including paint, labor, and overhead is ${netCost:0.2f}.")


if __name__ == "__main__":
    main()
