#fucntion to check whether palidrome or not 
def palind(r):
    e = len(r) -1
    s = 0 
    while(s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True



r = (1,2,3,2,3,1,1)

if(palind(r)):
    print("the tuple is Flip flo")
else:
    print("not floppy")

    