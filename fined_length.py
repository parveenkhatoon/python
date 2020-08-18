def check_length(user,user1):
    a=len(user)
    b=len(user1)
    if a>b:
        return(a,user)
    elif b>a:
        return(b,user1)
    else:
        return(a,(user),b,(user1))

