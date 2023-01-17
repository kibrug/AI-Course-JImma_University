class Person:
    def __init__(self,firstname,lname,age):
        self.fn=firstname
        self.ln = lname
        self.ag = age

    def printnamefunction(self,fn,ln,ag):
        """print("Enter first name")
        fn= input(self.firstname)
        print("Enter Last name")
        ln = input(self.lname)
        print("Enter age")
        ag = input(self.age)"""


        print(f"Your first name is {fn} and your last name is {ln} and your age is {ag} welcome this object orated coure in pythion")


"""
if __name__ == "__main__":
    main()
"""
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

"""
class Employee:
    def __init__(self,empfirstname,emplname,empsalary,empemail):
        self.empfirstname=empfirstname
        self.emplname= emplname
        self.empsalary= empsalary
        self.empemail= empemail

        def showEmployeeData(self):
            self.empfirstname = "kibeu"
            self.emplname= "G/m"
            self.empsalary= "50000000"
            self.empemail= "kibrug474@gmail.com"
            print(f"First name {self.empfirstname} last name is {self.emplname} salary is {self.empsalary} email is {self.empemail}")
        showEmployeeData(empfirstname,emplname,empsalary,empemail)





def main():

    """
    print("Enter first name")
    fn = input("firstname")
    print("Enter Last name")
    ln = input("lname")
    print("Enter age")
    ag = input("age")

    modified_data =Person()
    dat= modified_data.printnamefunction(fn,ln,ag)

    #print(modified_data)
    """
    data = Employee().empfirstname

if __name__ == "__main__":
    main()