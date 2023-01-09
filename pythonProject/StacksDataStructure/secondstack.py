
def addstackinjure():
    k= 6
    i=True
    stackdata= []
    """while i :

        print("Enter data")
        iall= input()
        if k==int(iall):
            break
        stackdata.append(iall)"""
    for  x in range(0,6):
        print("Enter data")
        iall = input()
        stackdata.append(iall)

        #stackdata.pop()
    """
    #stackdata.pop()
    #stackdata.append(8)
    #stackdata.count()
    #stackdata.sort()
    #stackdata
    #stackdata.push(9)

    
    #print(st)
    """
    print(stackdata)
    #print("Total"+stackdata.count())
    #print("sorted -1" + stackdata.sort(-1))
    #print("Index 3" + stackdata.index(3))
   # print("Remove 3" + stackdata.remove(3))
    print("Pop 5:" + stackdata.pop(3))
    print(stackdata)
addstackinjure()

