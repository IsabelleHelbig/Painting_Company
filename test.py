#Shiny Painting (SP) is looking to develop an application to streamline the quotation process
#The application will calculate the total interior surface area to be painted, amount of paint needed, total cost of the job including supplies and labour
#rooms have 4 walls, opposite walls are equal. Walls can be rectangular or square. Some rooms have fewer than or more than 4 walls. 

#main function
import math
gallonsamount = 350
gallonprice = 42.00

def main():
    print("Welcome to Shiny Paint Company for indoor painting!\n")
    roomnumber = int(input("How many rooms do you want to paint?: "))
    print("Thank you!")
    computeRoomArea(roomnumber)

def computeRoomArea(roomnumber):
    totalArea = 0
    totalGallons = 0
    totalPrice = 0
    paintPrice = 0
    labourcost = 0
    profitMargin = 0
    for i in range (0, roomnumber):
        print("\nRoom: ", i+1)
        roomselect = input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls, all square or rectangles)\n\nOption: ")
        while roomselect != "1" and roomselect != "2" and roomselect != "3":
            print("Error. Invalid value entered. Please try again.")
            roomselect = input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls, all square or rectangles)\n\nOption: ")
        roomselect = int(roomselect)
        if roomselect == 1:
            area = computeRectangleWallsArea()
            gallons = computeGallons(area)
            price = computePaintPrice(gallons)
        elif roomselect == 2:
            area = computeSquareWallsArea()
            gallons = computeGallons(area)
            price = computePaintPrice(gallons)
        elif roomselect == 3:
            area = computeCustomWallsArea()
            gallons = computeGallons(area)
            price = computePaintPrice(gallons)
        print(f"\nFor Room: {i+1}, Area to be painted is {area:.1f} square ft and will require {gallons:.2f} gallons to paint. The paint will cost approximately ${price:.2f}.")
        totalArea += area
        totalGallons += gallons
    totalGallons = math.ceil(totalGallons)
    paintPrice += totalGallons * 42.00
    labourcost = 0.15 * totalArea
    profitMargin = 0.30 * (paintPrice + labourcost)
    totalPrice = paintPrice + labourcost + profitMargin
    print(f"\nTotal area to be painted is {totalArea:.1f} square ft and will require {totalGallons} gallons to paint.\n The total customer estimate including paint, labor, and overhead is ${totalPrice:.2f}.")

def computeRectangleWallsArea():
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))
    return computeRectangleArea(length, width, height)

def computeRectangleArea(length, width, height):
    wall1 = (length*height)*2
    wall2 = (width*height)*2
    area = wall1 + wall2
    areaTotal = area - computeWindowsDoorsArea()
    return areaTotal

def computeSquareWallsArea():
    side = float(input("Enter one side length of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))
    return computeSquareArea(side, height)

def computeSquareArea(side, height):
    area = side*height*4
    areaTotal = area - computeWindowsDoorsArea()
    return areaTotal


def computeCustomWallsArea():
    walls = int(input("How many walls are there in the room? "))
    area = 0
    for i in range(0, walls):
        length = float(input(f"Enter the length of wall {i+1} in feet: "))
        height = float(input(f"Enter the height of wall {i+1} in feet: "))
        walls = length*height
        area += walls
    return area - computeWindowsDoorsArea()
    

def computeWindowsDoorsArea():
    windowDoor = int(input("\nHow many windows and doors are in the room? "))
    windowDoorAreaTotal = 0
    for i in range (0, windowDoor):
        length =  float(input(f"\nEnter window/door length for window/door {i+1} in feet: "))
        width = float(input(f"Enter window/door width for window/door {i+1} in feet: "))
        windowDoorArea = length*width
        windowDoorAreaTotal += windowDoorArea
    return windowDoorAreaTotal

def computeGallons(areaTotal):
    gallons = areaTotal/gallonsamount
    return gallons

def computePaintPrice(gallons):
    price = gallons * gallonprice
    return price


if __name__=='__main__':
    main()


