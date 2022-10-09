from BankClass import Bank
from CustomerClass import Customer
from flask import Flask,jsonify
#                (----------BankCLass--------)
print("------Create A Login Details for App-------")
name = str(input("Enter Your Full Name:"))
ph_num = int(input("Enter Your Phone number:"))
addres = str(input("Enter Your Addres:"))
pas = str(input("Password Only Letters:"))
re_enter = str(input("Renter Password:"))
info = {"Name": name,"Phone Number": ph_num,"Addres": addres,"Password": re_enter}
# file1 = open("D:\\New folder\\BankData.txt","a")
# file1.writelines(str(f"Details : {info}"))
# file1.close()

SBI =Bank(name,ph_num,addres,pas,re_enter)
print(SBI.create_login_details())
print(SBI.login())
print(SBI.bank_loan())

app = Flask(__name__)
tasks = [
    {
        "Logininfo":info
    },
]
@app.route("/tasks",methods=["GET"])
def get_tasks():
    return jsonify({"Tasks":tasks})
app.run(debug=True,port=8090)




#               (----------CustomerClass----------)
print("-------Personal Details TO Create Bank Account---------")
bank_name = str(input("IN Which Bank Do You Have To Open An Account:"))
my_name = str(input("Enter Your Full Name:"))
age = int(input("Age:"))
gender = str(input("Gender:"))
number = int(input("Enter 10 Digit Number:"))
addr = str(input("Enter Addres:"))
addhar = int(input("Addhar NO:"))
pan_card = int(input("Pan Card No:"))
ifsc = str(input("IFSC Code:"))
custinfo = {"Bank": bank_name,"Name": my_name,"Age": age,"Gender": gender,"Number": number,"Address": addr,"Addhar Card": addhar,"Pan Card": pan_card,"IFSC": ifsc}
file1 = open("D:\\New folder\\BankData.txt","a")
#file1.writelines(str(f"{bank_name}\n{my_name}\n{age}\n{gender}\n{number}\n{addr}\n{addhar}\n{pan_card}\n{ifsc}"))
file1.writelines(str(f"Details : {custinfo}"))
file1.close()

cust1 = Customer(bank_name,my_name,age,gender,number,addr,addhar,pan_card,ifsc)
print(cust1.create_account())
print(cust1.bank_account_id_pass())
print(cust1.deposit())
print(cust1.Withdraw())
print(cust1.transaction())
