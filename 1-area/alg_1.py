from decimal import Decimal

## Input -> Processes -> Output
## r        A = PI * r²    A

def area_of_circle(r: Decimal):
    PI: Decimal = 3.14
    area:Decimal  = PI * r**2
    print("CIRCLE",area)


area_of_circle(10)


def area_of_Parallelogram(b, h):
    area = b * h

    return area


print("Parallelogram",area_of_Parallelogram(5, 10))


def area_of_trapezoid(a, b, h):
    area = (a + b) / 2 * h
    return area


print("Trapezoid",area_of_trapezoid(10, 10, 5))
