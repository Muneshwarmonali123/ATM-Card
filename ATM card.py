balance=0
def Check_balance():
    print("Total Balance=",balance)
def deposit(amt):
    global balance
    balance=balance+amt
    print(amt,"Rs.deposited!")
def withdraw(amt):
    global balance
    if(balance>amt):
        balance=balance-amt
        print(amt,"Rs.withdrawn!")
    else:
        print("insufficient balance")
while True:
    ch=int(input("\n\n1.Deposit\t2.Withdraw\n3.Check Balance\t4.Exit"))
    if ch==1:
        print("Code for Deposit")
        d_amt=int(input("Enter amt to deposit:"))
        deposit(d_amt)
    elif ch==2:
        print("Code for Withdraw")
        w_amt=int(input("Enter amt to withdraw:"))
        withdraw(w_amt)
    elif ch==3:
        print("Code for Check Balance")
        Check_balance()
    elif ch==4:
        print("code for Exit")
        break
    else:
        print("Invalid Choice")
        
