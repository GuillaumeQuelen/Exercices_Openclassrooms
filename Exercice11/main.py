## Écrivez votre code ici !

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance :
            print("Retrait supérieur au solde")
        else:
            self.balance -= amount
    def display_balance(self):
        print(f"Utilisateur: {self.account_holder}\n  Solde: {self.balance}")

#Tests
account = BankAccount("Juju", 1290)
account.deposit(100)
account.withdraw(200)
account.display_balance()
account.withdraw(3000)
