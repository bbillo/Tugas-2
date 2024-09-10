n, pilar_a, pillar_b, pillar_c, pillar_d, = map(int,input().split())

#distance of each pillar

if n < pilar_a or n < pillar_b or n < pillar_c or n < pillar_d:
    print("NO HE CAN'T")
else:
    print("YES HE CAN")
