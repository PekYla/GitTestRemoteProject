import math

def CalcLogAreaOfCircle(iRadius):
    # Calc area of the circle
    iArea = math.pi * math.pow(iRadius, 2)
    print("Calc area of the circle:")
    print("Radius = ", iRadius)
    print("Area = ", iArea)

    # Write timestamp to log file
    f = open("tmp/Result.tmp", "w")
    f.write("Calc area of the circle:\n")
    f.write("Radius = %i\n" % (iRadius))
    f.write("Area = %i\n" % (iArea))
    f.close()