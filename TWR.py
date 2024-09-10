cat = list(map(int, input().split()))
cat_jumps = int(input())
jumps = int(input())

x, y, z = map(int, input().split())

for i in range (jumps):
    cat = cat[-cat_jumps:] + cat [:-cat_jumps]

print(cat[x], cat[y], cat[z])