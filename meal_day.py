
def  meal(day,time):
    if day=="sunday":
        if time=="breakfast":
            return "dosa"
        elif time=="lunch":
            return "dal rice"
        elif time=="dinner":
            return "paneer and  chapati"
        else :
            return "time not found"
    elif day=="monday":
        if time=="breakfast":
            return "fried rice"
        elif time=="lunch":
            return "aloo rice"
        elif time=="dinner":
            return "chhole bhature"
        else :
            return "time not found"
    elif day=="other":
        if time=="breakfast":
            return "aloo"
        elif time=="lunch":
            return "rajma rice"
        elif time=="dinner"    :
            return "veg-chapati"
        else :
            return "time not found"
day=input("Enter the day:")
time=input("Enter the time:")          
print(meal(day,time))


