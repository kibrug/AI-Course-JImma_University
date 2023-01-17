class Person:
    def __init__(self,firstname,lname,age):
        self.firstname=firstname
        self.lname = lname
        self.age = age

    def printnamefunction(self):
        print("Enter first name")
        fn= input(self.firstname)
        print("Enter Last name")
        ln = input(self.lname)
        print("Enter age")
        ag = input(self.age)


        print(f"Your first name is {fn} and your last name is {ln} and your age is {ag} welcome this object orated coure in pythion")

    printnamefunction()
"""
if __name__ == "__main__":
    main()
"""

class Car:
    def __init__(self,modelnamae):
        self.modelnamae= modelnamae

class Tata(Car):
    mnt = input("Enter Modele name")
    print(mnt)
class Handa(Car):
    hmn = input("Enter Modele name")
    print(hmn)