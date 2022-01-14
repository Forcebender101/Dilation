import replit
while 1==1:
  Transformation = input("Which Transformation would you like to do\n Di/Ro/Re/Tr\n").lower()
  if Transformation == "di":
    Scale = float(input("What is the scale factor\n"))
    replit.clear()
    Center = (
      float(input("What is the Point Of Dilation's X coordinate\n"))
      ,
      float(input("What is the Point Of Dilation's Y Coordinate\n"))
    )
    replit.clear()
    Shape = input("Are you Dilating a Triangle or a Point\n T/P\n").lower()
    replit.clear()
    if Shape == "p":
      Point = (
        float(input("What is the Points X coordinate\n"))
        ,
        float(input("What is the Points Y coordinate\n"))
      )
      replit.clear()
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
    elif Shape == "t":
      PointA = (
        float(input("What is the Point A's X coordinate\n"))
        ,
        float(input("What is the Point A's Y coordinate\n"))
      )
      replit.clear()
      PointB = (
        float(input("What is the Point B's X coordinate\n"))
        ,
        float(input("What is the Point B's Y coordinate\n"))
      )
      replit.clear()
      PointC = (
        float(input("What is the Point C's X coordinate\n"))
        ,
        float(input("What is the Point C's Y coordinate\n"))
      )
      replit.clear()
      #Do The Formula
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
      #Convert Variables to String
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
    else:
      print("I don't know that one")
  #Reflections
  elif Transformation == "re":
    print ("This currently only works with straight lines on one axis")
    Shape = input("Are you reflecting a Triangle or a Point\n (T/P)\n").lower()
    ReflectionAxis = input("Is your line to reflect on parralel to the y axis or the x axis\n (X/Y)\n").lower()
    if Shape == "t":
      if ReflectionAxis == "x":
        print ("hello world")
      elif ReflectionAxis == "y":
        print ("world hello")
      else:
        print ("I dont know that one")
    elif Shape == "p":
      Point = (
        float(input("What is the points X value\n"))
        ,
        float(input("What is the points Y Value\n"))
      )
      if ReflectionAxis == "x":
        RC = float(input("What is the Reflections Y Coordinate\n"))
        RP = str(RC - (Point[1] - RC))
        PointStr = (
          str(Point[0])
          ,
          str(Point[1])
        )
        print ("(" + PointStr[0] + "," + PointStr[1] + ") -> (" + PointStr[0] + "," + RP + ")")
      elif ReflectionAxis == "y":
        RC = float(input("What is the Reflections X Coordinate\n"))
        RP = str(RC - (Point[0] - RC))
        PointStr = (
          str(Point[0])
          ,
          str(Point[1])
        )
        print ("(" + PointStr[0] + "," + PointStr[1] + ") -> (" + RP + "," + PointStr[1] + ")")
      else:
        print ("I dont know that one")
    else:
      print ("I dont know that one")
  #Translations
  elif Transformation == "tr":
    Point = (
      float(input("What is the points X Value\n"))
      ,
      float(input("What is the Points Y Value\n"))
    )
    TC = (
      float(input("What is the Translations X Coordinate\n"))
      ,
      float(input("What is the Translations Y Coordinate\n"))
    )
    TP = (
      str(Point[0] + TC[0])
      ,
      str(Point[1] + TC[1])
    )
    PointStr = (
      str(Point[0])
      ,
      str(Point[1])
    )
    input("(" + PointStr[0] + "," + PointStr[1] + ") -> (" + TP[0] + "," + TP[1] + ")\n")
    