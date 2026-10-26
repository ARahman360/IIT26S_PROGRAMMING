from svgwrite import Drawing
import drawLib


def drawSquare(dwg: Drawing) -> None:
    print("Insert square")
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    drawLib.drawSquare(dwg, left=left, top=top, sideLength=side,
                       color=fill, strokeColor=stroke)


def drawCircle(dwg: Drawing) -> None:
    print("Insert circle")
    x = float(input("- Center X coord: "))
    y = float(input("- Center Y coord: "))
    radius = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    drawLib.drawCircle(dwg, centerX=x, centerY=y, radius=radius,
                       color=fill, stroke=stroke)


def saveSvg(dwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    answer = input("Proceed (y/n)?: ")
    if answer.lower() == "y":
        drawLib.saveSvg(dwg, filename)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")


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


if __name__ == "__main__":
    main()
