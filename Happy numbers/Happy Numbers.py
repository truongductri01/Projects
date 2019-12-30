'''A happy number is defined by the following process.
Starting with any positive integer, replace the number
by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Display an example of your output here. Find first 8 happy numbers'''

def square_sum(s): #calculate the sum of square values of a number's digits
    a=s
    sum=0
    while(a>0):
        sum+=pow(a%10,2)
        a=a//10
    return sum
def happy_check(s):
    result=0
    result=square_sum(s)
    count=0
    while True:
        if result==1:
            break
        elif result==4:
            break
        elif count>20:
            break
        result=square_sum(result)
        count+=1
    if result==1:
        arr.append(s)

if __name__=="__main__":
    arr=[]
    for s in range(1, 100):
        happy_check(s)
    print(arr)