class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def Addition(self):
        self.add=self.num1 + self.num2
        print("Addition is : ",self.add)

    def Subtraction(self):
        self.add=self.num1 - self.num2
        print("substraction is : ",self.add)

    def Multiplication(self):
        self.add=self.num1 * self.num2
        print("multiplication is : ",self.add)

    def Division(self):
        self.add=self.num1 / self.num2
        print("Division is : ",self.add)

while(True):
    ans=input("If you want to continue your calculation press(y)other wise enter else: ")
    if ans=='Y' or ans=='y':
        num1=int(input("Enter First Number : "))
        num2=int(input("Enter Second Number : "))
        cal=calculator(num1,num2)
        print("""Enter correct choice :-
press 1 for Addition:
press 2 for Subtraction:
press 3 for Multiplication:
press 4 for Division:
              """)
        
        a=int(input("enter you choice : "))
        match a:
            case 1:
                cal.Addition( )
            case 2:
                cal.Subtraction()
            case 3:
                cal.Multiplication()
            case 4:
                cal.Division()
            case _:
                    print("Enter valid choice ")
    else:
        print("exit your program successfully")
        break;