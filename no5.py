n = float(input("input the data usage in a month: "))

if 0.0 < n <= 1.0:
    print("charges: 250") 
elif 1.0 < n <= 2.0:
    print("charges: 500")
elif 2.0 < n <= 5.0:
    print("charges: 1000")
elif 5.0 < n <= 10.0:
    print("charges: 1500")
elif n >= 10.0:
    print("charges: 2000")
else:
    print("bad data")