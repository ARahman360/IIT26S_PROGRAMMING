"""Reusable SVG drawing helpers for week 8, task 6."""
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle


def drawSquare(dwg: Drawing, left: float, top: float, sideLength: float,
               color: str, strokeColor: str) -> None:
    dwg.add(Rect(insert=(left, top), size=(sideLength, sideLength),
                 fill=color, stroke=strokeColor))


def drawCircle(dwg: Drawing, centerX: float, centerY: float, radius: float,
               color: str, stroke: str) -> None:
    dwg.add(Circle(center=(centerX, centerY), r=radius,
                   fill=color, stroke=stroke))


def saveSvg(dwg: Drawing, filename: str) -> None:
    dwg.saveas(filename, pretty=True, indent=2)
