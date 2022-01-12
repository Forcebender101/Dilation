import replit
ScaleFactor = 0
PointOfDilationX = 0
PointOfDilationY = 0
PointX = 0
PointY = 0
DilatedPointX = 0
DilatedPointY = 0
Shape = 0
PointAX = 0
PointAY = 0
PointBX = 0
PointBY = 0
PointCX = 0
PointCY = 0
APrimeX = 0
APrimeY = 0
BPrimeX = 0
BPrimeY = 0
CPrimeX = 0
CPrimeY = 0
while 1==1:
  ScaleFactor = float(input("What is the scale factor\n"))
  PointOfDilationX = float(input("What is the point of dilations x coordinate\n"))
  PointOfDilationY = float(input("What is the point of dilations Y coordinate\n"))
  Shape = input("Are you Dilating a Triangle or a Point\n T/P\n").lower()
  if Shape == "p":
    PointX = float(input("What is the Points X coordinate\n"))
    PointY = float(input("What is the Points Y coordinate\n"))
    DilatedPointX = ScaleFactor * (PointX - PointOfDilationX) + PointOfDilationX
    DilatedPointY = ScaleFactor * (PointY - PointOfDilationY) + PointOfDilationY
    PointXStr = str(PointX)
    PointYStr = str(PointY)
    DilatedPointXStr = str(round(DilatedPointX,3))
    DilatedPointYStr = str(round(DilatedPointY,3))
    print ("("+ PointXStr +","+ PointYStr +") --> (" + DilatedPointXStr + "," + DilatedPointYStr + ")")
    input("")
    replit.clear()
  if Shape == "t":
    PointAX = float(input("What is the Point A's X coordinate\n"))
    PointAY = float(input("What is the Points A's Y coordinate\n"))
    PointBX = float(input("What is the Point B's X coordinate\n"))
    PointBY = float(input("What is the Points B's Y coordinate\n"))
    PointCX = float(input("What is the Point C's X coordinate\n"))
    PointCY = float(input("What is the Points C's Y coordinate\n"))
    APrimeX = ScaleFactor * (PointAX - PointOfDilationX) + PointOfDilationX
    APrimeY = ScaleFactor * (PointAY - PointOfDilationY) + PointOfDilationY
    BPrimeX = ScaleFactor * (PointBX - PointOfDilationX) + PointOfDilationX
    BPrimeY = ScaleFactor * (PointBY - PointOfDilationY) + PointOfDilationY
    CPrimeX = ScaleFactor * (PointCX - PointOfDilationX) + PointOfDilationX
    CPrimeY = ScaleFactor * (PointCY - PointOfDilationY) + PointOfDilationY
    PointAXStr = str(PointAX)
    PointAYStr = str(PointAY)
    PointBXStr = str(PointBX)
    PointBYStr = str(PointBY)
    PointCXStr = str(PointCX)
    PointCYStr = str(PointCY)
    APrimeXStr = str(round(APrimeX,3))
    APrimeYStr = str(round(APrimeY,3))
    BPrimeXStr = str(round(BPrimeX,3))
    BPrimeYStr = str(round(BPrimeY,3))
    CPrimeXStr = str(round(CPrimeX,3))
    CPrimeYStr = str(round(CPrimeY,3))
    print ("A(" + PointAXStr  +","+ PointAYStr +") B(" + PointBXStr + "," + PointBYStr + ") C("+ PointCXStr + "," + PointCYStr + ") \n --> A'(" + APrimeXStr + "," + APrimeYStr + ") B'(" + BPrimeXStr + "," + BPrimeYStr + ") C'("+ CPrimeXStr + "," + CPrimeYStr + ")")
    input("")
    replit.clear()