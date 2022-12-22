"""1 Sum Two number from user"""
firstnumbr = int(input("Enter First number\n"))
second = int(input("Enter Second Number\n"))
SumofTwoNumber= firstnumbr + second
print(f"Sum of Two Number is {SumofTwoNumber}")

""" 2 Data type list ,tuple,set dec"""
# List Data Type
listdatatype=[1,3,'helo',67,90]
print(f"List Data Type {listdatatype}")

#Tuple data type
tupledatatype=(1,3,'helo',67,90)
print(f"Tuple Data Type {tupledatatype}")

#Set data type
setdatatype={1,'kibru',67,"hello"}
print(f"Set Data Type {setdatatype}")

#Dic data type
dictdatatype={"name":"kibru","age":25,"From":'Durame'}
print(f"Set Data Type {dictdatatype}")


#dict to list
#print("Dict To list "+list(dictdatatype))

#set to List
#print("Dict To Tuple "+list(setdatatype))

# 3 Average of Five Number
def sumoffivenumber():
    try:
        a= int(input("Enter Fist Int Number\n"))
        b = int(input("Enter Second Int Number\n"))
        c = int(input("Enter Threed Int Number\n"))
        d = int(input("Enter Fourth Int Number\n"))
        e = int(input("Enter Last Int Number\n"))
        SumOfFiveNumber= a+b+c+d+e
        averageofFiveNumber = SumOfFiveNumber/5
        #Average of Five Number
        print(f"Average of Five Number: {averageofFiveNumber}")
    except:
        print("Place Enter Correct Data Type")

sumoffivenumber()

# 4 Swap Two number
def swepTwoNumber():
    try:
        firstnumbrtoSwep = input("Enter Fist Number")
        secondnumbrtoSwep = input("Enter Fist Number")
        withoutswep =  firstnumbrtoSwep + secondnumbrtoSwep
        print(f"without swep : {withoutswep}")
        # After swep
        # This Is First Way To Do Sewepe
        swn = secondnumbrtoSwep +firstnumbrtoSwep
        print(F"after sweep:{swn}")

        # This Is Second Way To Do Sewepe

        firstnumbrtoSwep =secondnumbrtoSwep
        sweplist =firstnumbrtoSwep
        firstnumbrtoSwep=sweplist




        sweplist =[]
        #for i in range(0,2):
           # sweplist.append(i)

            #print(F"after sweep second way:{sweplist}")



    except:
        print("Try agin")



swepTwoNumber()


def checkEvenOrOdd():

    firsttrycheck = int(input("Enter number"))

    if firsttrycheck%2==0:
        print(f"Even Number: {firsttrycheck} ")
    elif firsttrycheck%2==1:
        print(f"Odd Number: {firsttrycheck} ")
    else:
        print( "Try agn")
checkEvenOrOdd()

def checkLaragestNumber():
    firstnubers = int(input("Enter first number"))
    secondnubers = int(input("Enter Second number"))
    threednubers = int(input("Enter Threed number"))
    if firstnubers >= secondnubers:
        if firstnubers >= threednubers:
            print(f"Largest Number is : {firstnubers}")
        else:
            print(f"Largest Number is : {threednubers}")
    elif secondnubers >= threednubers :
        if secondnubers >= firstnubers:
            print(f"Largest Number is : {secondnubers}")
        else:
            print(f"Largest Number is : {firstnubers}")
    else:
        print("try")
checkLaragestNumber()

# 7 BMI calculate Body Mass index
def bodyMassIndexCallcultion():
    massofperson = float(input("Enter mass of your body"))
    heightofperson = float(input("Enter height of your body"))
    massIndex = massofperson /(heightofperson *heightofperson )
    print(f"Body Mass Of Your Body Is : {massIndex} KG/M2")
bodyMassIndexCallcultion()

def simpleCalculater():
    fistn= int(input("Enter your Number\n"))
    secn = int(input("Enter your Second Number\n"))
    print("What to Do Now \n")
    print("Enter ")
    print("+")
    print("-")
    print("/")
    print("*")
    sum= input(print("+ \n"))
    sub = input(print("- \n"))
    mult = input(print("* \n"))
    div = input(print("/ \n"))

    if sum:
        sumn =fistn + secn
        print(f"Sum of Your Number is :{sumn}")
    elif sub:
        sumn = fistn - secn
        print(f"subtraction of Your Number is :{sumn}")
    elif mult:
        sumn = fistn * secn
        print(f"subtraction of Your Number is :{sumn}")
    elif div:
        sumn = fistn * secn
        print(f"subtraction of Your Number is :{sumn}")
    else:
        print("Try")

simpleCalculater()























