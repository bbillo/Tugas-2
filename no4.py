color = input("enter the first letter of the cylinder's color (o, b, y, g.): ").strip().lower()

if color == "o":
    print("ammonia")
elif color == "b":
    print("carbon monoxide")
elif color == "y":
    print("hydrogen")
elif color == "g":
    print("oxygen")
else:
    print("contents unknown")