def askDimension(PPrompt: str) -> float:
    feed = float(input(f"Insert {PPrompt}: "))
    return feed


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    area = PWidth * PHeight
    return area


def main() -> None:
    print("Program starting.")
    width = askDimension("width")
    height = askDimension("height")
    area = calcRectangleArea(width, height)
    print()
    print(f"Area is {area}²")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
