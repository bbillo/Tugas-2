HH, MM, SS = map(int,input().split(":"))
CH, CM, CS = map(int,input().split(":"))

#convert to GMT + 7
HH = HH + 5

#convert to seconds
stream_time = (HH * 3600) + (MM * 60) + SS
ali_time = (CH * 3600) + (CM * 60) + CS

time_difference = stream_time - ali_time

if time_difference < 0:
    print("See you on the next Pear Event!")

else:
    hour = time_difference // 3600
    time_difference %= 3600
    munite = time_difference // 60
    seconds = time_difference % 60
    print(f'{hour:02}:{munite:02}:{seconds:02}')