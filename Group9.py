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
# Author Andy Lee, Isabelle Helbig, Ekom Uffort
# Version 2022-11-18

import math

#constant values
labourCost = 0.15
profit_margin = 0.3
paintCoverageSquareFeetPerGallon = 350.0
paintGalloncost = 42.0

#function defining the begining of the program
def main():
    print("Welcome to Shiny Paint Company for indoor painting!\n")

    numRoom = int(input("How many rooms do you want to paint?: "))
    print("Thank you!")

    netCost, netArea =0, 0,
    for i in range(1, 1+ numRoom):
        netArea += computeRoomArea(i)
    
    #calculations for the final message
    netGallons = math.ceil(netArea/350)
    
    #Cost per gallon of paint
    netCost += netGallons*paintGalloncost
    
    #Labour cost per feet squared
    netCost +=labourCost*netArea
    
    #Profit margin (30 percent)
    netCost += netCost*profit_margin
    
    print(f"\n\nTotal area to be painted is {netArea:0.1f} square ft and will require {netGallons} gallon(s) to paint.\nThe total customer estimate including paint, labor, and overhead is ${netCost:0.2f}.")

#Function defining compute room area   
def computeRoomArea(roomNum):
    #display instructions
    print(f"""\nRoom: {roomNum}
Select the shape of the room:
1 – Rectangular
2 – Square
3 - Custom (more or less than 4 walls, all square or rectangles)

Option: """, end='')

    #get input from user
    roomShape =int(input()) 
    
    #option for if the user picks rectangular
    if roomShape == 1:
        area = computeRectangleWallsArea()
    
    #option for if the user picks square
    elif roomShape == 2:
        area = computeSquareWallsArea()
    
    #option for if the user picks custom
    elif roomShape == 3:
        area = computeCustomWallsArea()
    
    #message for each room total
    gallons = computeGallons(area)
    cost = computePaintPrice(area)
    print(f"\n\nFor Room: {roomNum}, Area to be painted is {area:0.1f} square ft, and will require {gallons:0.2f} gallons to paint. The paint will cost approximately: ${cost:0.2f}")
    return area

#function defining the rectangular walls area
def computeRectangleWallsArea():
    length = float(input("Enter the length of room length in feet: "))
    width = float(input("Enter the width of room width in feet: "))
    height = float(input("Enter the height of room height in feet: "))
    
    #calling upn the compute rectangle area function
    frontArea = computeRectangleArea(length,height)
    sideArea = computeRectangleArea(height,width)
    surfaceArea = (2*sideArea) + (2*frontArea)

    #calling upon the compute window/door area function
    windowDoorArea = computeWindowsDoorsArea()
    return (surfaceArea -windowDoorArea)

def computeRectangleArea(base,height):
    return (base*height)

def computeSquareWallsArea ():
    length = float(input("Enter one side length of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))

    #calling upn the compute sqaure area function
    surfaceArea = computeSquareArea(length,height)

    #calling upon the compute window/door area function
    windowDoorArea = computeWindowsDoorsArea()
    return(4*surfaceArea - windowDoorArea)

#Function defining the square area  
def computeSquareArea(length,height):
    return length*height

#function defining the windows and door areas   
def computeWindowsDoorsArea():
    area = 0
    numWindowOrDoors =  int(input("\nHow many windows and doors are in the room? "))
    print()
    for i in range(1, 1+numWindowOrDoors):
        length = float(input(f"Enter the window/door length for window/door {i} in feet: "))
        width = float(input(f"Enter the window/door width for window/door {i} in feet: "))
        area += length*width
    return area

#function defining the custom walls area
def computeCustomWallsArea():
    area = 0
    numWalls = int(input("How many walls are there in the room? "))
    #Area of each wall
    for i in range(1, 1+ numWalls):
        length = float(input(f"What is the length for wall {i} in feet: "))
        height = float(input(f"What is the height for wall {i} in feet: "))
        area += length*height
    windowDoorArea = computeWindowsDoorsArea()
    #Return net surface area
    return area - windowDoorArea

#function definign gallons needed
def computeGallons(area):
    return (area /paintCoverageSquareFeetPerGallon)

#function defining paint price
def computePaintPrice(area):
    cost = computeGallons(area)*paintGalloncost
    answer = (round(cost, 2))
    return answer

#calling upon the function 
if __name__ == "__main__":
    main()