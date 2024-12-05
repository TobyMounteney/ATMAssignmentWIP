user = {
    'pin': '9999'
    'balance' '500'
    }

print("Welcome to the Toby ATM")
pin = int(input{"Insert your pin now (For testing purposes, your pin is 9999)"})
          if pin == user['Pin']
          print("Enter 1 if you wish withdraw cash. 2 if you wish to see balance. 3 if you wish to deposit cash or 4 if you wish to see your recent transactions")
          if input == 1:
          withdrawal()
          if input ==2:
              balance()
          if input == 3:
              deposit()
        else if input == 4:
            transactions()
              
        else:
            print("That is not an option. Enter 1 if you wish withdraw Cash or 2 if you wish to see balance.")
        else:("Wrong Pin, Please retry")

def withdrawal():
    amount = int(input("Enter the amount you'd like to take out")
                 if amount > user['balance']
                 print("Insufficient funds")
                else:
                    user['Balance'] = user['balance'] - amount
                    print [{amount}" successfully taken out"]

def balance():
print user['balance'}

def deposit():
    amount = int(input("Enter the amount you'd like to deposit")
                 user['Balance'] = user['balance'] + amount
                 print [{amount}" successfully taken out"]

def transactions():
