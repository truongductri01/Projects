def square_sum(s): #calculate the sum of square values of a number's digits
    a=s
    sum=0
    while(a>0):
        sum+=pow(a%10,2)
        a=a//10
    return sum

def happy_check(s):
    result=square_sum(s)
    print(s)
    print("Start of function")
    print(result)
    count=0
    while True:
        if result==1:
            break
        elif result==4:
            break
        elif count>20:
            break
        result=square_sum(result)
        print(result)
        count+=1
    print("Final result: {} after {} counts".format(result,count))
    print("")
    return result

# def testing(s):
#     if happy_check(s)==4 or happy_check(s)==1:
#         return "Yes: {}".format(happy_check(s))
#     else:
#         return "No: {}".format(happy_check(s))

if __name__=="__main__":
    f=open("Test Numbers") #test each number from the code
    arr=list(map(int,f.readline().split(", ")))
    print(arr)
    for x in arr:
        happy_check(x)
    f.close()

    # for s in range(1,1000):
    #     print(s,end=" ")
    #     print(testing(s))