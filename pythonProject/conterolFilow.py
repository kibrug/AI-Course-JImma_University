# if clouse
from re import match


def inputnumber():
    n= int(input("Enter number That betwen of one and ten\n"))
    try:
        if n ==0:
            print("your enter is :"+ n)
        elif n==1:
            print("Your Enter of is "+ n)
        elif n==2:
            print("Your Enter of is "+ n)
        elif n == 3:
            print("Your Enter of is " + n)
        elif n == 4:
            print("Your Enter of is " + n)
        elif n == 5:
            print("Your Enter of is " + n)
        elif n == 6:
            print("Your Enter of is " + n)
        elif n == 7:
            print("Your Enter of is " + n)
        elif n == 8:
            print("Your Enter of is " + n)
        elif n == 9:
            print("Your Enter of is " + n)
        elif n == 10:
            print("Your Enter of is " + n)
        else:
            print("Try Agn")
    except:
        print("Error occure")

inputnumber()

# for loops
def foorloops():

    lstword = [1,3,'kibru','hi', 78,45]
    for w in lstword:
        print(w)
foorloops()


# Range function
print("Range function")
def rangeFunction():

    for i in  range(10):
        print(i)
rangeFunction()

# range Function  with list data

def rangefunctionWithList():
    listdata = ['hello',45,78,'youare fine ',56,870,'look it good']
    for k in range(len(listdata)):
        print(k,listdata[k])
rangefunctionWithList()

# Break statement
def rangeFunctionbreak():

    for i in  range(10):
        if i == 5:
            break

        print(i)
rangeFunctionbreak()
#    continue function that used to jump that stat
def rangeFunctioncontines():

    for i in  range(10):
        if i == 5:
            continue

        print(i)


rangeFunctioncontines()

# match Statements other language that is Switch stataement

def matchstataement(n):
    n.match(6)

    while True:

        print("True")
    print("That is Good state")
matchstataement(6)

















