
class BankAccount:

    MIN_BALANCE = 1000

    def __init__(self, owner,account_no):
        self.owner = owner
        self.account_no = account_no
        self._balance = 0
    
    def deposite(self, deposite_amount):
        self._deposite_amount = deposite_amount
        if self._deposite_amount < 0:
            print("Deposite amount cannot be less than 0")
        else:
            if self._balance + self._deposite_amount < BankAccount.MIN_BALANCE:
                print(f"Deposite Failed as Balance after deposite is less than Minimum Balance of {BankAccount.MIN_BALANCE}")
            else:
                self._balance += self._deposite_amount
                print(f"Amount {self._deposite_amount} has been deposited to {self.owner}'s account {self.account_no}")
                self.__log_transaction("Deposite", self._deposite_amount)
                self._get_balance()
    
    def _get_balance(self):
        print(f"Balance amaount available for {self.owner} is {self._balance}")

    def __log_transaction(self,transaction_type, amount):
        print(f"Transaction {transaction_type} done is {amount}")
    

user1 = BankAccount("Dan", "AC_001")
user1.deposite(1500)




            