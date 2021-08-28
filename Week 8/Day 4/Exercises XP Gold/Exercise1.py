class BankAccount():
    def __init__(self,username,password,balance = 0,authenticated = False,):
        self.authenticated = authenticated
        self.username = username
        self.password = password
        self.balance = balance
    

    def deposit(self,amount: int):
        if amount<0:
            raise Exception("Amount has to be positive")
        elif self.authenticated == False:
            raise Exception("Account isn't authenticated")
        else:
            self.balance += amount


    def withdraw(self,amount: int):
        if amount<0:
            raise Exception("Amount has to be positive")
        elif self.authenticated == False:
            raise Exception("Account isn't authenticated")
        else:
            self.balance -= amount
    

    def authenticate(self,username,password):
        if self.username == username and self.password == password and self.authenticated == True:
            return True
        elif self.username == username and self.password == password and self.authenticated is not True:
            return True
        else:
            return False


class MinimumBalanceAccount(BankAccount):
    def __init__(self,username,password,balance = 0,minimum_balance = 0,authenticated = False):
        self.minimum_balance = minimum_balance
        super().__init__(username,password,balance,authenticated)


    def withdraw(self,amount: int):
        if amount<0:
            raise Exception("Amount has to be positive")
        elif self.authenticated == False:
            raise Exception("Account isn't authenticated")
        elif self.balance-amount<self.minimum_balance:
            raise Exception("balance can't be lower than defined minimum balance")
        else:
            self.balance -= amount


class ATM:
    current_tries = 0
    def __init__(self,account_list,try_limit):
        for account in account_list:
            if not isinstance(account,(BankAccount,MinimumBalanceAccount)):
                raise Exception ("Not all accounts on account_list are a BankAccount or MinimumBalanceAccount")
        self.account_list = account_list
        self.try_limit = try_limit
        try:
            if try_limit>0:
                pass
            else:
                raise Exception ("Not a positive number,try_limit set to two")
        except Exception as e:    
            print(e)
            self.try_limit = 2
    

    def show_main_menu(self):
        while True:
            if self.current_tries >= self.try_limit:
                return '' #maximum amount of login's reached
            menu = input(
            '''
Main Menu:
Log in
Exit
Please select an option: ''')
            if menu.capitalize() == 'Exit':
                return print('Thank you for using our ATM, have a good day.')
            elif menu.capitalize() == 'Log in':
                username = input("Please enter your username: ")
                password = input("Please enter your password: ")
                self.log_in(username,password)
                if self.current_tries == self.try_limit:
                    return ''
            else:
                print("\nInvalid input,please select again: ")


    def log_in(self,username,password):
        for i in range(len(self.account_list)):
            if self.account_list[i].authenticate(username,password):
                if self.show_account_menu(self.account_list[i]) == False:
                    return ''
        self.current_tries+=1
        if self.current_tries == self.try_limit:
            return print("You have reached the maximum log in attempts,good day")
        print("No match,please try with another account:")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        self.log_in(username,password)

    
    def show_account_menu(self,account):
        while True:
            menu = input('''
Account Menu:
Deposit
Withdraw
(Exit) To Main Menu
Please select an option: ''')
            if menu.capitalize() == 'Exit':
                print('Thank you for using our ATM, have a good day.')
                return False
            elif menu.capitalize() == 'Deposit':
                deposit_amount = int(input("How much would you like to deposit? "))
                account.deposit(deposit_amount)
            elif menu.capitalize() == 'Withdraw':
                withdraw_amount = int(input("How much would you like to withdraw? "))
                account.withdraw(withdraw_amount)
            else:
                print("\nInvalid input,please select again: ")

Ofer = BankAccount('Ofer','Secret',150,True)
Jeff = BankAccount('Jeff','123',191800000000,True)
account_list = [Ofer,Jeff]
test = ATM(account_list,5)
test.show_main_menu()
print(Jeff.balance)