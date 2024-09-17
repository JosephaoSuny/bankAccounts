from threading import Lock, Thread

class BankAccount:
    def __init__(self, initial_balance: int):
        self.initial_balance = initial_balance
        self.mutex = Lock()
            
    def withdraw(self, amount: int) -> int:
        print("Calling withdraw, amount = ", amount)
        self.mutex.acquire(blocking=True)

        if amount > self.initial_balance:
            print("Amount too great!")
            raise Exception("Withdraw would overdraft")

        self.initial_balance -= amount

        self.mutex.release()

        return amount
    
    def deposit(self, amount: int) -> int:
        self.mutex.acquire(blocking=True)
        self.initial_balance += amount
        self.mutex.release()
        return amount
    
PhilsBankAccount = BankAccount(10)
    
t = Thread(target=PhilsBankAccount.withdraw, args=[11])
t.start()

t.join()

print(PhilsBankAccount.initial_balance)