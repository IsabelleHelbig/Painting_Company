# Assignment3 - CPRG216
#
#The application calculates the total interior surface area to be painted, the amount of paint needed, and the total cost of the job, 
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
# Author Ekom Uffort
# Version 2022-11-14

import math

#constant values
labourCost = 0.15
profit_margin = 0.3
paintCoverageSquareFeetPerGallon = 350.0
paintGalloncost = 42.0

#function defining the begining of the program
def main():
    print ("Welcome to Shiny Paint Company for indoor painting!\n")
    numberOfRooms = int(input("How many Rooms do you want to paint? "))
    print ("Thank You!")
    computeRoomArea(numberOfRooms)

#Function defining compute room area    
def computeRoomArea(numberofRooms):
    for i in range(1, numberofRooms + 1):
        print (f"\nRoom: {i}")
        print ("Select the shape of the room: \n 1 - Rectangular \n 2 - Square \n 3 - Custom (more or less than 4 walls, all square or rectangles)")
        option = input(int("Option: "))
        
        #option for if the user picks rectangular
        if option == 1:
            roomLength = float(input ("Enter the length of the room in feet: "))
            roomWidth = float(input ("Enter the width of the room in feet: "))
            roomHeight = float(input ("Enter the height of the room in feet: "))
            rectangleArea = computeRectangleWallsArea(roomLength, roomWidth, roomHeight)
            windowDoorArea = computeWindowsDoorsArea()
            return rectangleArea - windowDoorArea
        
        #option for if the user picks square
        elif option == 2:
            roomLength = float(input("Enter one side length of room in feet: "))
            roomHeight = float(input("Enter the height of room in feet: "))
            rectangleArea = computeSquareArea(roomLength, roomHeight)
            windowDoorArea = computeWindowsDoorsArea()
            return rectangleArea - windowDoorArea

        #option for if th user picks custom
        elif option == 3: 
            numberCustomWalls = int(input ("How many walls are there in the room: "))
            customWallArea = 0
            for m in range(1, numberCustomWalls + 1):
                roomLength = float(input(f"Enter the length of the wall {m} in feet: "))
                roomHeight = float(input(f"Enter the height of the wall {m} in feet: "))
                customWallArea = customWallArea + (roomLength * roomHeight)
            windowDoorArea = computeWindowsDoorsArea()
            return customWallArea - windowDoorArea

        areaTotal = 0.0 
        paintArea = computeRoomArea(numberOfRooms)
        totalgallon = computeGallons (paintArea)

        print ("For Rooms: {0}, Area to be painted is {1: .1f} square ft and will require {2: .2f} gallons to paint. The paint will cost approcimately ${3: .2f}.".format(i, paintArea, totalgallon, computePaintPrice(totalgallon)))

        areaTotal = areaTotal + paintArea
    totalgallon = math.ceil(computeGallons(areaTotal))
    print ("Total area to be painted is {0: .1f} square ft and will require {1} gallons to paint. The total customer estimate including paint, labour, and overhead is ${2: .2f}".format(areaTotal, totalgallon, computePriceTotal(totalgallon, areaTotal)))
                
#function defining the rectangular walls area
def computeRectangleWallsArea(roomLength, roomWidth, roomHeight):
    rectangleArea = ((2 * (roomLength * roomHeight)) + (2 * (roomWidth * roomHeight)))
    return rectangleArea

#function defining the windows and door areas   
def computeWindowsDoorsArea():
    windowDoorArea = 0.0
    numberWindowDoor = int(input("\nHow many windows and doors are in the room? "))
    for i in range(1, numberWindowDoor + 1):
        roomLength = float(input("Enter window/door length for window/ door {} in feet: ".format(i)))
        roomWidth = float(input("Enter window/door width for window/ door {} in feet: ".format(i)))
        windowDoorArea = (windowDoorArea + (roomLength * roomWidth))
    print()
    return windowDoorArea

#Function defining the square area   
def computeSquareArea(roomLength, roomHeight):
    return ((roomHeight * roomLength) * 4)

#function definign gallons needed
def computeGallons(paintArea):
    return paintArea / paintCoverageSquareFeetPerGallon

#function defining paint price
def computePaintPrice(gallon):
    return (gallon * paintGalloncost)

#function defining price total
def computePriceTotal(gallon, area):
    return ((gallon * paintGalloncost) + (labourCost * area)) * (profit_margin + 1)


#calling upon the function 
if __name__ == "__main__":
    main()
    