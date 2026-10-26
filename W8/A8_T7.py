import math
from svgwrite import Drawing
from svgwrite.shapes import Polygon
from A8_T6 import drawSquare, drawCircle, saveSvg


def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon details:")
    middle_x = float(input("Middle point X: "))
    middle_y = float(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    radius = apothem / math.cos(math.radians(30))
    points = []
    for index in range(6):
        angle = math.radians(-60 + index * 60)
        x = round(middle_x + radius * math.cos(angle))
        y = round(middle_y + radius * math.sin(angle))
        points.append((x, y))

    hexagon = Polygon(points=points, fill=fill, stroke=stroke)
    PDwg.add(hexagon)
    return None


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")
    return None


def main() -> None:
    drawing = Drawing()
    print("Program starting.")
    while True:
        showOptions()
        choice = input("Your choice: ")
        if choice == "1":
            drawSquare(drawing)
        elif choice == "2":
            drawCircle(drawing)
        elif choice == "3":
            drawHexagon(drawing)
        elif choice == "4":
            saveSvg(drawing)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
        print()

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
