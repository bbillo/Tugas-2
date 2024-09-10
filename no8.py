print("(1) first service")
print("(2) second service")

service = input("enter free service number (1)/(2): ").strip().lower()
miles = int(input("enter the number of miles: "))

if service == "1":
    if 1500 < miles <= 3000:
        print("vehicle must be serviced")
    else:
        print("vehicle musn't be serviced")
elif service == "2":
    if 3001 < miles < 4500:
        print("vehicle must be serviced")
    else:
        print("vehicle musn't be serviced")
else:
    print("invalid service number choose between (1) or (2)")

