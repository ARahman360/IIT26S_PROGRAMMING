def askDimension(PPrompt: str) -> float:
    number = float(input("Insert " + PPrompt + ": "))
    return number


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    area = PWidth * PHeight
    return area


def main():
    print("Program starting.")
    width = askDimension("width")
    height = askDimension("height")
    area = calcRectangleArea(width, height)
    print()
    print("Area is " + str(area) + "²")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
