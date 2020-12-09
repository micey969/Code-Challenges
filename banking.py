import os
from time import sleep

class Bank():

    customerInfo = []

    def AddCustomer(self, customer):
        os.system("clear")
        accountNew = self.AssignAcctNumber() #gets a new account number to assign to customer
        customer.accountNumber = accountNew #saves the account number to the customer object
        self.customerInfo.append(customer) #adds the customer information to the list of customers

        print("\n\n\tThank you for choosing Bank of SVG.")
        print("\n\tYour account number is "+str(accountNew))
        sleep(2)
        welcome()
        

    def AssignAcctNumber(self):
        startingNum = 1000
        return startingNum + len(self.customerInfo) #returns an incremental account number


    def __PrintSheet__(self):
        sleep(2)
        os.system("clear")
        print("\tAccount Number \t Customer Name \t Customer Address \t Customer email \t Customer Number \t Customer DOB \t Customer Pin \t Customer Balance\n")
        for customer in self.customerInfo:
            print("\n\t"+str(customer.accountNumber)+" \t \t "+customer.fullName+" \t \t "+customer.address+" \t \t "+customer.email+" \t \t"+customer.number+" \t \t "+customer.dob+" \t \t "+str(customer.pin)+"\t \t"+str(customer.balance))



class Customer():

    def __init__(self,name, addr, dob, tel, email, pin):
        self.fullName = name
        self.address = addr
        self.dob = dob
        self.number = tel
        self.email = email
        self.pin = pin
        self.transactions = []
        self.balance = 0.00
        self.accountNumber = 0


    def Display(self):
        sleep(2)
        os.system("clear")
        print("\n\tCustomer Name: "+self.fullName)
        print("\n\tCustomer Address: "+self.address)

        print("\n\tTYPE \t\t\t AMOUNT")
        for transaction in self.transactions:
            tranType, tranAmount = transaction
            print("\n\t"+tranType+" \t\t $%.2f" %(tranAmount))
        sleep(3)
        menu(self.accountNumber)


    def Deposit(self):
        sleep(2)
        os.system("clear")
        deposit = float(input("\tEnter the amount you would like to deposit: "))
        while deposit < 0:
            deposit = float(input("\tEnter the amount you would like to deposit: "))
        self.balance += deposit
        print("\n\t$%.2f has been deposited to you account. Your new balance is $%.2f" %(deposit, self.balance))
        self.transactions.append(("\tDeposit", deposit))
        menu(self.accountNumber)


    def Inquiry(self):
        sleep(2)
        os.system("clear")
        print("\n\tAvailable Balance  is $%.2f" %(self.balance)) 
        menu(self.accountNumber)


    def Transfer(self):
        sleep(2)
        os.system("clear")
        account = int(input("\tEnter the recipient's account number: "))

        for bankAcct in bosvg.customerInfo:
            if bankAcct.accountNumber == account:
                amount = float(input("\tEnter the amount to be transferred: "))
                if self.balance >= amount: 
                    self.balance -= amount
                    bankAcct.balance += amount
                    self.transactions.append(("\tTransfer (W)", amount))
                    print("\tYou have transferred $%.2f to account number %s."%(amount, account))
                    bankAcct.transactions.append(("T\transfer (D)", amount))
                    menu(self.accountNumber)
                else: 
                    print("\n\t Insufficient balance: $%.2f" %(self.balance)) 
                    menu(self.accountNumber)

        print("\n\n\tThe Account number does not exist.")
        menu(self.accountNumber)

  
    def Withdraw(self):
        sleep(2)
        os.system("clear")
        amount = float(input("\tEnter the amount to be withdrawn: ")) 
        if self.balance >= amount: 
            self.balance -= amount 
            print("\n\t$%.2f has been withdrawn from your account." %(amount)) 
            print("\tYour balance is $%.2f" %(self.balance))
            self.transactions.append(("\tWithdraw", amount))

        else: 
            print("\n\t Insufficient balance: $%.2f" %(self.balance)) 
        menu(self.accountNumber)

    
    def Update(self):
        sleep(2)
        os.system("clear")

        print("\t \t Welcome to Bank Of SVG")
        print("\t \tThe bank that gives you more.\n\n")

        print("\n\t To update your banking information, please re-enter the following information with the updates.\n")
        name = raw_input("\tPlease enter your first and last name: ")
        address = raw_input("\tPlease enter your address: ")
        number = raw_input("\tPlease enter your contact number: ")
        email = raw_input("\tPlease enter your email address: ")
        pin = int(input("\tPlease enter a four (4) digit pin number: "))

        while len(str(pin)) != 4:
            print("\tPin not recognised. Please try again.\n")
            pin = int(input("\tPlease enter a four (4) digit pin number: "))

        #update customer account
        self.fullName, self.address, self.number, self.email, self.pin = name, address, number, email, pin
        
        #update banking records
        for bankAcct in bosvg.customerInfo:
            if self.accountNumber == bankAcct.accountNumber:
                bankAcct.fullName, bankAcct.address, bankAcct.number, bankAcct.email, bankAcct.pin = name, address, number, email, pin

        print("\t\nPlease log back in to save updates.")
        login()



def check_login(acct,pin):
    sleep(2)
    os.system("clear")

    for bankAcct in bosvg.customerInfo:
        if bankAcct.accountNumber == acct and bankAcct.pin == pin:
            return 1
        elif bankAcct.accountNumber == acct or bankAcct.pin == pin:
            return 2

    return 0


def login():
    sleep(2)
    os.system("clear")
    attempts = 0


    print("\t \t Welcome to Bank Of SVG")
    print("\t \tThe bank that gives you more.\n\n")
    while attempts < 3:
        acc = int(input("\tEnter Account Number: "))
        pin =  int(input("\tEnter Pin: "))

        if check_login(acc,pin) == 1:
            menu(acc)
        elif check_login(acc,pin) == 2:
            print("\tLogin Unsuccessful. Please try again.")
            attempts += 1
        else:
            print("\tAccount Number not recognise. Please register first.")
            register()

    print("\tToo many unsuccessful login attempts. Please try again in 2 minutes.")
    sleep(120)
    welcome()


def menu(acct):
    sleep(2)
    os.system("clear")

    #get the customer information
    for bankAcct in bosvg.customerInfo:
        if bankAcct.accountNumber == acct:
            customer = bankAcct


    print("\t \tMENU")
    print("\t1 - WITHDRAW")
    print("\t2 - INQUIRY")
    print("\t3 - DEPOSIT")
    print("\t4 - TRANSFER")
    print("\t5 - BANK STATEMENT")
    print("\t6 - UPDATE CUSTOMER INFORMATION")
    print("\t0 - EXIT")

    choice = int(input("\tPlease enter your menu item number: "))
    while choice < 0  or choice > 6:
        print("\tOption not recognised. Please try again.\n")
        choice = int(input("\tPlease enter your menu item number: "))

    if choice == 1:
        customer.Withdraw()
    elif choice == 2:
        customer.Inquiry()
    elif choice == 3:
        customer.Deposit()
    elif choice == 4:
        customer.Transfer()
    elif choice == 5:
        customer.Display()
    elif choice == 6:
        customer.Update()
    else:
        print("\n\tThanks for banking with us. Good bye.")
        exit()


def register():  
    sleep(2)  
    os.system("clear")

    print("\t \t Welcome to Bank Of SVG")
    print("\t \tThe bank that gives you more.\n\n")
    name = raw_input("\tPlease enter your first and last name: ")
    address = raw_input("\tPlease enter your address: ")
    dob = raw_input("\tPlease enter your DOB (dd-mm-yyyy): ")
    number = raw_input("\tPlease enter your contact number: ")
    email = raw_input("\tPlease enter your email address: ")
    pin = int(input("\tPlease enter a four (4) digit pin number: "))

    while len(str(pin)) != 4:
        print("\tPin not recognised. Please try again.\n")
        pin = int(input("\tPlease enter a four (4) digit pin number: "))

    #create the new customer account
    customer = Customer(name,address,dob,number,email,pin)
    deposit = float(input("\tEnter at least a minimum deposit of $10.00: "))
    while self.balance == 0 and deposit < 10:
        deposit = float(input("\tEnter at least a minimum deposit of $10.00: "))
    customer.balance += deposit
    customer.transactions.append(("\tDeposit", customer.balance))
    bosvg.AddCustomer(customer)
    login()
  

def startScreen():
    sleep(2)
    os.system("clear")
    print("\t \tMENU")
    print("\t1 - LOGIN")
    print("\t2 - REGISTER")
    print("\t0 - EXIT")

    choice = int(input("\tPlease enter your menu item number: "))
    while choice < 0  or choice > 2:
        print("\tOption not recognised. Please try again.\n")
        choice = int(input("\tPlease enter your menu item number: "))

    if choice == 1:
        login()
    elif choice == 2:
        register()
    else:
        print("\n\tThanks for banking with us. Good bye.")
        exit()


def welcome():
    os.system("clear")
    print("\t \t Welcome to Bank Of SVG")
    print("\t\tThe bank that gives you more.")
    sleep(2)


def main():
    #set up the banking environment
    global bosvg
    bosvg = Bank()

    #add the five dummy accounts
    #first dummy account
    first = Customer('Bridget Patterson','Canouan','19-04-1965','784-455-4808','cbrowne@gmail.com',1118)
    first.balance = 10.00
    first.transactions.append(("\tDeposit", first.balance))
    bosvg.AddCustomer(first)

    #second dummy account
    second = Customer('Joseph Browne','Vermont','19-11-1963','784-493-1708','josephbrowne@gmail.com',3827)
    second.balance = 10.00
    second.transactions.append(("\tDeposit", second.balance))
    bosvg.AddCustomer(second)

    #third dummy account
    third = Customer('Shamiann Alexander','England','07-07-1986','784-526-6906','salexander@hotmail.com',7788)
    third.balance = 10.00
    third.transactions.append(("\tDeposit", third.balance))
    bosvg.AddCustomer(third)

    #fourth dummy account
    fourth = Customer('Nirel Johnson','Largo Heights','01-01-1999','784-431-1478','nirelljohnson@gmail.com',1199)
    fourth.balance = 10.00
    fourth.transactions.append(("\tDeposit", fourth.balance))
    bosvg.AddCustomer(fourth)

    #fifth dummy account
    fifth = Customer("Na'Kayla Forbes",'Chataeubelair','25-12-2019','784-456-1234','nkforbes@gmail.com',2512)
    fifth.balance = 10.00
    fifth.transactions.append(("\tDeposit", fifth.balance))
    bosvg.AddCustomer(fifth)

    #start the banking app
    welcome()
    startScreen()
    # bosvg.__PrintSheet__()

if __name__ == "__main__":
    main()
 