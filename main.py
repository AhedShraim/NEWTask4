# Create a python program which includes a main menu
# 1. Sum
def add(x,y):
    total = x + y
    return total
# 2. Subtract
def sub(x,y):
    total = x - y
    return total
# 3. Multiply
def mul(x,y):
    total = x * y
    return total
# 4. Division
def div(x,y):
    total = x / y
    return total
# 5. Calculate triangle area
def area_tri(base,length_tri):
    total = 0.5 * base * length_tri
    return total
# 6. Calculate circle area
def area_cir():
    total = math.pi * (radius**2)
    return total
# 7. Calculate rectangle area
def area_rec(length_rec,width):
    total = length_rec * width
    return total

while True:
    print("\nMAIN MENU")
    print("1. Calculate addition process")
    print("2. Calculate subtraction process")
    print("3. Calculate division process")
    print("4. Calculate multiplication process")
    print("5. Calculate Area of a Triangle")
    print("6. Calculate Area of a Circle")
    print("7. Calculate Area of a rectangle")
    print("8. Exit")
    choice1 = int(input("Enter the Choice: "))

    if choice1 == 1:
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        total = add(num1, num2)
        print("Total of the addition process is: ", total)
    elif choice1 == 2:
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        total = sub(num1, num2)
        print("Total of the subtraction process is: ", total)

    elif choice1 == 3:
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        total = div(num1, num2)
        print("Total of the division process is: ", total)

    elif choice1 == 4:
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        total = mul(num1, num2)
        print("Total of the multiplication process is: ", total, "\n")
    elif choice1 == 5:
            # You have to ask the user for Base and length for triangle area
            base = float(input("Enter the Base of the triangle: "))
            length_tri = float(input("Enter the Length of the triangle: "))
            total = area_tri(base, length_tri)
            print("The area of the triangle is: ", total, "\n")
        # 6. Calculate circle area
    elif choice1 == 6:
            import math
            # Radius for circle area
            radius = float(input("Enter the Radius of the circle: "))
            total = area_cir()
            print("The area of the circle is: ",total,"\n")
        # 7. Calculate rectangle area
    elif choice1 == 7:
            # Length and width for rectangle area
           length_rec = float(input("Enter the Length of the rectangle: "))
           width = float(input("Enter the Width of the rectangle: "))
           total = area_rec(length_rec,width)
           print("The area of the rectangle is: ",total,"\n")
        # 8. Exit
    elif choice1 == 8:
        break

    else:
        print("Sorry !!!,Invalid Input.")