N, C = map(int, input().split())
if N % 3 == 0:
    if C == 1:
        print("Lili")
    else:
        print("Lala")
else:
    if C == 1:
        print("Lala")
    else:
        print("Lili")