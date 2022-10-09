import random
class Customer:
    account_user = 0 
    def __init__(self,bank_name,my_name,age,gender,number,addr,addhar,pan_card,ifsc):
        self.bank_name = bank_name
        self.my_name = my_name 
        self.number = number
        self.addr = addr
        self.addhar = addhar
        self.pan_card = pan_card
        self.age = age 
        self.gender = gender
        self.ifsc = ifsc   
        Customer.account_user += 1 
        self.balance = 0 
        self.ac_no = int(random.random()*100000000)
    @classmethod
    def get_account_user(cls):
        return cls.account_user 
    def create_account(self):
        return f"*********Account Create is Successful{self.my_name}!! Thanks For Coming Bank***********"
    def bank_account_id_pass(self):
        #account = int(random.random()*100000000)
        print("-------Company Provide Your Account Number---------")
        print(f"Conform Bank Account Number {self.ac_no}")
        account_no = int(input("Enter your account Number:"))
        password = str(input("Enter your password: "))
        confirm = str(input("conform Password:"))
        file1 = open("D:\\New folder\\BankData.txt","a")
        file1.writelines(str(f'Account Number: {account_no}\nPassword: {confirm}'))
        file1.close() 
        if self.ac_no == account_no :
            True
            if password == confirm:
                True
            else:
                raise ("!@#$&8--ERROR Type Correct Password--!@#%&")
        else:
            raise ("!@#$%^--ERROR Insufficient Account Number--^%$#@!")
        return f"Your Bank account Number is {account_no} and Your password is {password}\n thank"

    def deposit(self):
        deposit_amount =float(input("How Much Amount would you like to Deposit:"))
        self.balance += deposit_amount
        file1 = open("D:\\New folder\\BankData.txt","a")
        file1.write(f"Deposit: {deposit_amount}")
        file1.close()
        return f"You Have Succsefully Deposit RS.{deposit_amount}\nYour Updated balance is RS.{self.balance}"
    def Withdraw(self):
        amount =float(input("How Much would You like To Withdraw:"))
        if self.balance > amount:
            self.balance -= amount
            file1 = open("D:\\New folder\\BankData.txt","a")
            file1.write(str(f"Withdraw : {amount}")) 
            file1.close() 
            return (f"********You Have Succsefully:{amount}*********\nAccount balance has been Updeted: {self.balance}")
        else:
            return {"Insufficient balance":self.balance}
    def transaction(self):
        amount= int(input("Enter your transaction Amount:"))
        account_no = int(input("Enter 8 Digit Account Number To Transaction:"))
        dit = {"Amount": amount,"Account No": account_no}
        if self.balance > amount:
            self.balance -= amount
            if self.ac_no == account_no:
                pass
            else:
                raise ("!@#$%^Please Enter Valid Account Number!@#$%^")
            file1 = open("D:\\New folder\\BankData.txt","a")
            file1.writelines(str(f"Transation :{amount}\tBalance : {self.balance}"))
            file1.close()
            return (f'''Succsefully Transaction To This Accoount:{account_no}\nTransaction Amount: {amount}\nAmount Balance Has been Updeted:{self.balance}''')
        else:
            return f"*****Transaction Has Been Declined by Bank*******"


    




        

#cust1 = Customer("Hdfc","vaibhav patil",23,"male",8652300144,"mumbai",651656165,65165355,"sbi55")
#print(cust1.create_account())
#print(cust1.bank_account_id_pass())
#print(cust1.deposit())
#print(cust1.Withdraw())
#print(cust1.transaction())
