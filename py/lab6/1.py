class Password_Manager:
    def __init__(self,*args):
        self.old_password=[x for x in args]        

    def get_password(self):
        return self.old_password[-1]
    
    def set_password(self,string):
        for x in self.old_password:
            if x==string:
                return "it is old password!\ncan't change passowrd"
        self.old_password.append(string)       
        return "Password changed succesfully"

    def is_correct(self,string):
        if string==self.old_password[-1]:
            return True
        else:
            return False

vamsi=Password_Manager("vamsi","vamsi baludu","balu@2006","bv@08")
a=True
while a:
    print("1.Get_Password\n2.set_Password\n3.Verification\n4.Exit\nSelect:",end=" ")
    choice=int(input())
    match choice:
        case 1: print(f"your password is {vamsi.get_password()}")

        case 2: 
                string=input("Enter Pasword: ")
                print(f"{vamsi.set_password(string)}") 

        case 3: 
                string=input("Enter Pasword: ")
                print("Correct Password!" if vamsi.is_correct(string) else "Invalid Passsword!")

        case 4:a=False
    print()
                                               


