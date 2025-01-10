import time
t=(time.strftime("%H:%M:%S"))
hour=int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
    print("Good Moring Sir !!")
elif(hour>=12 and hour<16):
    print("Good Afternoon Sir !!")
# elif(hour>=17 and hour<0):
else:
    print("Good Night Sir !!")
