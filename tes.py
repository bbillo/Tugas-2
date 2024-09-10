M, N, T = map(int, input().split())

red = 20
yellow = 5
green = 60
total_cars = M + N
cycle_time = 20 + 5 + 60

full_cycles = T // cycle_time

remaining_time = T % cycle_time

cars_passed = full_cycles * 12

if remaining_time > red + yellow:
    extra_green_time = remaining_time - (red + yellow)
    cars_passed += extra_green_time // 5

if cars_passed == M:
    print(f"NO! {N + 1}")

elif cars_passed > M:
    remaining_cars = total_cars - cars_passed
    if remaining_cars < 0:
        remaining_cars = 0
    print(f"YES! {remaining_cars}")
else:
    cars_left = total_cars - cars_passed
    print(f"NO! {cars_left + 1}")