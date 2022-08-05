#                                  Banking Management System
import mysql.connector as c
class BankSystem:
    def welcome(self):
        print(50*" ",30*"*")
        print(50*" ","BANK MANAGEMENT SYSTEM")
        print(50*" ",30 * "*")
        print(50*" ","Brought to you by: Jasmeet Kaur")

    def mainmenu(self):
        print(10*" ","MAIN MENU:")
        print(10*" ","1.OPEN ACCOUNT")
        print(10*" ","2.DEPOSIT AMOUNT")
        print(10*" ","3.WITHDRAW AMOUNT")
        print(10*" ","4.ACCOUNT DETAILS")
        print(10*" ","5.CHECK BALANCE")
        print(10*" ","Press any key to exit")
    def openAccount(self):
        try:
            Acc_num=int(input("Enter Account Number:"))
            Acc_holder=input("Enter Account Holder Name:")
            Acc_type=input("Enter type of account [C/S]:")
            ini_amt =float(input("Enter the initial amount(>= 500) for saving and (>=1000)  for current"))
            # User database for current account
            if Acc_type.capitalize() == "C":
                if ini_amt>=1000:
                    query = f"Insert into user values({Acc_num},'{Acc_holder}','{Acc_type}',{ini_amt})"
                    cursor.execute(query)
                    con.commit()
                    print("Account Created Successfully!!!!")
                else:
                    print("Amount should be greater than Rs.1000")
            if Acc_type.capitalize() == "S":
                if ini_amt >= 500:
                    query = f"Insert into user values({Acc_num},'{Acc_holder}','{Acc_type}',{ini_amt})"
                    cursor.execute(query)
                    con.commit()
                    print("Account Created Successfully!!!!")
                else:
                    print("Amount should be greater than Rs.500")
        except:
            print("Enter Valid input")
    def balance(self):
        try:
            acc_num = int(input("Enter Account Number:"))
            query= f"Select Account_num,initial_amt from user"
            cursor.execute(query)
            x = cursor.fetchall()
            for x,y in x:
                if x==acc_num:
                    print(f"Account Number:{x}\nBalance:{y}")
        except Exception as e:
            print(e)


    def details(self):
        try:
            acc_num = int(input("Enter Account Number:"))
            query= f"Select * from user"
            cursor.execute(query)
            x = cursor.fetchall()
            for i in x:
                if i[0]==acc_num:
                    print(f"Account Number: {i[0]}\n"
                          f"Name: {i[1]}\n"
                          f"Account Type: {i[2]}\n"
                          f"Balance: {i[3]}\n")
        except Exception as e:
            print(e)
    def cash_deposit(self):
        try:
            acc_num = int(input("Enter Account Number:"))
            amount = int(input('Enter the amount you want to deposit'))
            query=f"Update user set initial_amt =initial_amt+{amount} where Account_num={acc_num}"
            cursor.execute(query)
            con.commit()
            print(f"Rs.{amount} Deposited Successfully!!")
        except:
            print("Enter Valid input!!")
    def cash_Withdraw(self):
        try:
            acc_num = int(input("Enter Account Number:"))
            amount = int(input('Enter the amount you want to Withdraw'))
            query = f"Update user set initial_amt =initial_amt-{amount} where Account_num={acc_num}"
            cursor.execute(query)
            con.commit()
            print(f"Rs.{amount} Withdrawn Successfully!!")
        except:
            print("Enter Valid input!!")

if __name__ == '__main__':

    con = c.connect(host="localhost",user="root",passwd="*********",database="bankdb")
    # Acts like a bridge to transfer data
    cursor = con.cursor()
    b = BankSystem()
    b.welcome()
    while(1):
        b.mainmenu()
        answer=input("Enter choice: ")
        if answer=="1":
            b.openAccount()
        elif answer=="2":
            b.cash_deposit()
        elif answer =="3":
            b.cash_Withdraw()
        elif answer=="4":
            b.details()
        elif answer=="5":
            x = b.balance()
        else:
            print("THANK YOU!!!")
            break

