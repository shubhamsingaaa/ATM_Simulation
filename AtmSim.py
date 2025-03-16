import time

print("Please Insert Your Card")

time.sleep(5)

password = 1234
pin=int(input("Enter Your ATM PIN: "))
balance = 5000
    

if pin==password:
    while True:
        print("""
        1 : Balance Enquiry
        2 : Withdraw Balance
        3 : Deposite Balance
        4 : Exit
        """)

        try:
            option = int(input("Please Enter Your Choice: "))
        except:
            print("Please Enter Valid Option")


        if option == 1:
            print("------------------------------------------")
            print(f"Your Current Balance is {balance}")

        if option ==2:
            withdraw_amount =  int(input("Enter Amount to Withdraw: "))
            balance -= withdraw_amount
            print("------------------------------------------")
            print(f" {withdraw_amount} is debited from your Account.")
            print(f" Your Updated Balance is : {balance}")
            print("------------------------------------------")

        if option == 3:
            deposite_amount = int(input("Enter Deposite Amount: "))
            balance += deposite_amount
            print("------------------------------------------")
            print(f"{deposite_amount} is credited to your Account")
            print(f"Your Updated Balance is : {balance}")
            print("------------------------------------------")

        if option == 4:
            break


else:
    print("Wrong PIN, Please try again...")