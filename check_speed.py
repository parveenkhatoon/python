def speed_checking(speed):
    score=speed-70
    point=score//5
    if point>12:
        return(point,"license suspended")
    if speed<=70:
        return("ok")
    if speed>70:
        return(point,"this speed 70 corse")
speed=int(input("Enter the speed"))
print(speed_checking(speed))