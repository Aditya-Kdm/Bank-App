
class Bank:
    def __init__(self,name,ph_num,addres,pas,re_enter):
        self.name = name 
        self.ph_num = ph_num
        self.addres = addres
        self.pas = pas
        self.re_enter = re_enter
    def create_login_details(self):
        if self.pas == self.re_enter:
            True
        else:
            raise ("!@$%^&*--ERROR Wrong Password--!@#$%^&*")
        return f"*******Welcome TO My Bank App********\n!!!!!Thanks for Using App!!!!!"
        
    def login(self):
        print("-----Login Your Account------")
        n =str(input("Login Name:"))
        number = int(input("Phone Number:"))
        password = str(input("Password:"))
        log = {"Name": n,"Number": number,"Password": password}   
        file1 = open("D:\\New folder\\BankData.txt","a")
        file1.writelines(str(f"Login : {n}\nPassword: {password}"))
        file1.close()
        if self.pas == password:
            True
            if self.name == n:
                True
                if self.ph_num == number:
                    True
                else:
                    raise ("!@#$%^&*--ERROR Incorrect Number--*&^%$#@!")
            else:
                raise ("!@#$%^&*--ERROR Incorrect Name--*&^%$#@!")
        else:
            raise ("!@#$%^&*--ERROR Incorrect Password--*&^%$#@!")
        return f"!!!!!!!Welcome MY Bank App This Your Login detalis {log}!!!!!!!!!!\n ***** How Can I Help You *****"

    def bank_loan(self):
        option = int(input("1)if You Want A Loan prees (1): 2)To Exit press (2): "))
        if option == 1:
            return("For Bank Loan Or Gold Loan Contact Company Help line Number: 9562400155")
        elif option == 2:
            return ("More Details : Help Line Number (9989765688)")

#SBI =Bank("vaibhav patil",8652300144,"mumbai","vaibhav7","vaibhav7")

#print(SBI.create_login_details())
#print(SBI.Login())
#print(SBI.bank_loan())