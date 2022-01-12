import replit

while 1==1:
  Scale = float(input("What is the scale factor\n"))
  Center = (
    float(input("What is the Point Of Dilation's X coordinate\n")),
    float(input("What is the Point Of Dilation's Y Coordinate\n"))
  )
  Shape = input("Are you Dilating a Triangle or a Point\n T/P\n").lower()
  if Shape == "p":
    Point = (
      float(input("What is the Points X coordinate\n"))
      ,
      float(input("What is the Points Y coordinate\n"))
    )
    DilatedPoint =(
      Scale * (Point[0] - Center[0]) + Center[0]
      ,
      Scale * (Point[1] - Center[1]) + Center[1]
    )
    PointStr =(
      str(Point[0])
      ,
      str(Point[1])
    )
    DilatedPointStr = (
      str(round(DilatedPoint[0],3))
      ,
      str(round(DilatedPoint[1],3))
    )
    print ("("+ PointStr[0] +","+ PointStr[1] +") --> (" + DilatedPointStr[0] + "," + DilatedPointStr[1] + ")")
    input("")
    replit.clear()
  if Shape == "t":
    PointA = (
      float(input("What is the Point A's X coordinate\n"))
      ,
      float(input("What is the Point A's Y coordinate\n"))
    )
    PointB = (
      float(input("What is the Point B's X coordinate\n"))
      ,
      float(input("What is the Point B's Y coordinate\n"))
    )
    PointC = (
      float(input("What is the Point C's X coordinate\n"))
      ,
      float(input("What is the Point C's Y coordinate\n"))
    )
    APrime = (
     Scale * (PointA[0]- Center[0]) + Center[0]
      ,
     Scale * (PointA[1] - Center[1]) + Center[0]
    )
    BPrime = (
     Scale * (PointB[0]- Center[0]) + Center[0]
      ,
     Scale * (PointB[1] - Center[1]) + Center[0]
    )
    CPrime = (
     Scale * (PointC[0]- Center[0]) + Center[0]
      ,
     Scale * (PointC[1] - Center[1]) + Center[0]
    )
    PointAStr = (
     str(PointA[0])
     ,
     str(PointA[1])
    )
    PointBStr = (
     str(PointB[0])
     ,
     str(PointB[1])
    )
    PointCStr = (
     str(PointC[0])
     ,
     str(PointC[1])
    )
    APrimeStr = (
     str(APrime[0])
     ,
     str(APrime[1])
    )
    BPrimeStr = (
     str(BPrime[0])
     ,
     str(BPrime[1])
    )
    CPrimeStr = (
     str(CPrime[0])
     ,
     str(CPrime[1])
    )
    replit.clear()
    print ("A(" + PointAStr[0] + "," + PointAStr[1] + ") --> A'(" + APrimeStr[0] + "," + APrimeStr[1] + ")\n")
    print ("B(" + PointBStr[0] + "," + PointBStr[1] + ") --> B'(" + BPrimeStr[0] + "," + BPrimeStr[1] + ")\n")
    print ("C(" + PointCStr[0] + "," + PointCStr[1] + ") --> C'(" + CPrimeStr[0] + "," + CPrimeStr[1] + ")\n")
    input("")
    replit.clear()