#function activity 2 - cash machine
pin_number = 22
balance = int(2000)

def withdraw_cash(pin,amount):
    if pin_number == pin and balance > amount:
        new_balance =  balance - amount
        print("dispensing cash and your current balance is £{}".format(new_balance))
    elif pin_number == pin or balance != amount:
        print("insufficient funds")
    else:
        print("incorrect pin")

withdraw_cash(22,200)
withdraw_cash(2,300)

#cash machine - liam's solution
#variables
actual_pin = 1234
balance = 500

#function 
def cash_machine(pin,amount):
    #logic if statements
    if pin == actual_pin and amount <= balance
    new_bal = balance - amount
    print("take your cash of £{}. Your new balance iis £{}".format(amount,new_bal))






