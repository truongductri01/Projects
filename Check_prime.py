import math
def prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        if n%2==0:
            #print(2)
            return False
        else:
            r=int(math.sqrt(n))+1
            for i in range (3, r, 2):
                if n%i==0:
                    #print("i:",i)
                    return False
            return True

if __name__=="__main__":
    try:
        n=11375995735515375997
        print(len(str(n)))
        print(prime(n))
    except:
        print(Exception)