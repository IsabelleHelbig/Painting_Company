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
# Author Ekom Uffort, Isabelle Helbig, Andy Lee
# Version 2022-11-14

import math


#constant values
labourCost = 0.15
profit_margin = 0.3
paintCoverageSquareFeetPerGallon = 350.0
paintGalloncost = 42.0

#main function. Used to display introduction message and ask for the room number
def main():
    print("Welcome to Shiny Paint Company for indoor painting!\n")
    roomnumber = int(input("How many rooms do you want to paint?: "))
    print("Thank you!")
    computeRoomArea(roomnumber)

def computeRoomArea(roomnumber):
    totalArea = 0
    totalGallons = 0
    paintPrice = 0
    #asking for room shape and sending down to the calculation functions
    for i in range (0, roomnumber):
        print("\nRoom: ", i+1)
        roomselect = input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls, all square or rectangles)\n\nOption: ")
        while roomselect != "1" and roomselect != "2" and roomselect != "3":
            print("Error. Invalid value entered. Please try again.")
            roomselect = input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls, all square or rectangles)\n\nOption: ")
        roomselect = int(roomselect)
        if roomselect == 1:
            area = computeRectangleWallsArea()
        elif roomselect == 2:
            area = computeSquareWallsArea()
        elif roomselect == 3:
            area = computeCustomWallsArea()
        #calculating the gallons and price for each room and then printing the total message for each room
        gallons = computeGallons(area)
        price = computePaintPrice(gallons)
        print(f"\nFor Room: {i+1}, Area to be painted is {area:.1f} square ft and will require {gallons:.2f} gallons to paint. The paint will cost approximately ${price:.2f}.")
        #adding each room's area and paint needed to the total bill
        totalArea += area
        totalGallons += gallons
    #the calculations for the total bill and the final print message
    totalGallons = math.ceil(totalGallons)
    paintPrice += totalGallons * paintGalloncost
    labour = labourCost * totalArea
    profitMargin = profit_margin * (paintPrice + labour)
    totalPrice = paintPrice + labour + profitMargin
    print(f"\nTotal area to be painted is {totalArea:.1f} square ft and will require {totalGallons} gallons to paint.\n The total customer estimate including paint, labor, and overhead is ${totalPrice:.2f}.")

#taking the input for the rectangle walls and sending it to the calculator function
def computeRectangleWallsArea():
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))
    return computeRectangleArea(length, width, height)

#calculating the rectangle room and sending to window/door calculator then subtracting the window/door area and returning the area value 
def computeRectangleArea(length, width, height):
    wall1 = (length*height)*2
    wall2 = (width*height)*2
    area = wall1 + wall2
    areaTotal = area - computeWindowsDoorsArea()
    return areaTotal

#taking the input for the square room
def computeSquareWallsArea():
    side = float(input("Enter one side length of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))
    return computeSquareArea(side, height)

#the calculation for the square room, subtracting window/door area and returning the value
def computeSquareArea(side, height):
    area = side*height*4
    areaTotal = area - computeWindowsDoorsArea()
    return areaTotal

#calculating custom rooms through input of the amount of walls and asking the measurements of each wall
#subtracts window/door area and returns area value
def computeCustomWallsArea():
    walls = int(input("How many walls are there in the room? "))
    area = 0
    for i in range(0, walls):
        length = float(input(f"Enter the length of wall {i+1} in feet: "))
        height = float(input(f"Enter the height of wall {i+1} in feet: "))
        area += length*height
    return area - computeWindowsDoorsArea()  

#taking the number of windows/doors and calculating their areas and sending the value back to the calulation for each room
def computeWindowsDoorsArea():
    windowDoor = int(input("\nHow many windows and doors are in the room? "))
    windowDoorAreaTotal = 0
    for i in range (0, windowDoor):
        length =  float(input(f"\nEnter window/door length for window/door {i+1} in feet: "))
        width = float(input(f"Enter window/door width for window/door {i+1} in feet: "))
        windowDoorAreaTotal += length*width
    return windowDoorAreaTotal

#function for calulating the gallons needed per room
def computeGallons(area):
    gallons = area/paintCoverageSquareFeetPerGallon
    return gallons

#function for calulating the price for the amount of gallons needed
def computePaintPrice(gallons):
    price = gallons * paintGalloncost
    return price

if __name__=='__main__':
    main()
