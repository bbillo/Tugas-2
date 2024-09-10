x = float(input("input the x coordinate: "))
y = float(input("input the y coordinate: "))

if x == 0 and y == 0:
    print("is in the center point")
elif x == 0:
    print("is on the y-axis")
elif y == 0:
    print("is on the x-axis")
elif x > 0 and y > 0:
    print("is in quadrant I")
elif x > 0 and y < 0:
    print("is in quadrant IV")
elif x < 0 and y > 0:
    print("is in quadrant II")
elif x < 0 and y < 0:
    print("is in quadrant III")