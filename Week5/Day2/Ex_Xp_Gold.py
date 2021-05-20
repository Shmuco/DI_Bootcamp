class bank_account():
    def __init__(self, balance, username, password, authenticated= False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated
    
    def authenticate(self, username, password):
        if username == self.username & password==self.password:
            self.authenticated = True

    
    def deposit(self, amount):
        if self.authenticated == True:
            if amount>0:
                self.balance+=amount
            else:
                print("Please enter a positive number") 
        else: print('Please authenticate')
    
    def withdraw(self, amount):
        if self.authenticated == True:
            if amount>0:
                self.balance-=amount
            else:
                print("Please enter a positive number") 
        else: print('Please authenticate')
    

class minimum_balance_account(bank_account):
    def __init__(self,minimum_balance = 0):
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if self.balance>self.minimum_balance:
            if amount>0:
                self.balance-=amount
            else:
                return "Please enter a positive number."
        else: return "Your balance is below the minimum balance."


class ATM():
    def __init__(self,account_list, try_limit):
        # for i in account_list:
        #     if isinstance(i,minimum_balance_account,bank_account):
        #         return
        #     else: 
        #         print('error')
        # if try_limit>2
        pass
    def show_main_men()
