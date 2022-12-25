
print("Enter following Character")
print("for sum +")
print("for subteraction -")
print("for divesion /")
print("for multipution *")
def calculaterAll():
    print("Enter first Number \n")
    n= float(input())
    print("Enter + or - or / or * Number \n")
    c=input()
    print("Enter second Number")
    scn = float(input())


    if c== '+':
        sum = n + scn
        print("Sum is :"+sum)
    elif c=='-':
        sub = n - scn
        print("substeraction of two number is :"+sub)
    elif c == '*':
        mul = n * scn
        print("multplaction of two number is :" + mul)

    elif c == '/':
        div = n / scn
        print("Divesion  of two number is :" + div)
    else:
        print("Try agn")

calculaterAll()








