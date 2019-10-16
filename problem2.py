import math
import problem2

def circle_area(radius):
    area = math.pi * radius * radius
    return round(area,2)

def circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return round(circumference,2)

def square_area(side):
    area = side * side
    return round(area,2)

def square_perimeter(side):
    perimeter = 4 * side
    return round(perimeter,2)

def rectangle_area(length, breath):
    area = length * breath
    return round(area,2)

def rectangle_perimeter(length, breath):
    perimeter = 2 * (length + breath)
    return round(perimeter,2)

def main():
    while True:
        choice = str(input("Choose a shape: (C)ircle or (R)ectangle or (S)quare: "))
        if ( choice == 'R'):
            length = int(input("Enter length: "))
            breath = int(input("Enter breath: "))
            print("Area: ",rectangle_area(length,breath)," square units and Perimeter: ",rectangle_perimeter(length,breath)," units")  
        elif  ( choice == 'S'):
            side = int(input("Enter side: "))
            print("Area: ",square_area(side)," square units and Perimeter: ",square_perimeter(side)," units")
            
        elif  ( choice == 'C'):
            radius = int(input("Enter radius: "))
            print("Area: ",circle_area(radius)," square units and Perimeter: ",circle_circumference(radius)," units")  

if __name__ == "__main__":
    main()


    

