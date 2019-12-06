import math
import Check_prime as CK

def factor(n):
    a=n
    r=math.ceil(n/2)
    result=""
    print("r:",r)
    print("a:",a)
    while True:
        if CK.prime(n) or CK.prime(a):
            result=result+"*"+str(a)
            print("Run through Prime")
            break
        count = 0
        if a%2==0:
            result = result + "*" + str(2)
            a = a // 2
            print("i:", 2, "a:", a)
            print("factor:", result)
        else:
            for i in range(3, r+1, 2):
                if CK.prime(i) and a%i == 0:
                    result = result + "*" + str(i)
                    a = a // i
                    print("i:", i, "a:", a)
                    print("factor:", result)
                    break
        if r>a:
            r=a
        if a==1 or a==n:
            print("Run through")
            break
        print("r:", r)
    result=result.replace('*','',1)
    print("Result: ", result)
if __name__=="__main__":
    # n=int(input("Input value to begin factoring: "))
    try:
        n=1358
        print(len(str(n)))
        factor(n)
    except:
        print(Exception)