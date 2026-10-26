from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle


def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    square = Rect(insert=(left, top), size=(side, side), fill=fill, stroke=stroke)
    PDwg.add(square)
    return None


def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    x = float(input("- Center point X: "))
    y = float(input("- Center point Y: "))
    radius = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    circle = Circle(center=(x, y), r=radius, fill=fill, stroke=stroke)
    PDwg.add(circle)
    return None


def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print('Saving file to "{}"'.format(filename))
    answer = input("Proceed (y/n)?: ")
    if answer.lower() == "y":
        PDwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")
    return None


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
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
