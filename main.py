from threading import Lock, Thread
from typing import List
import random

class BankAccount:
    def __init__(self, initial_balance: int):
        self.initial_balance = initial_balance
        self.mutex = Lock()
            
    def withdraw(self, amount: int) -> int:
        self.mutex.acquire(blocking=True)

        if amount > self.initial_balance:
            raise Exception("Withdraw would overdraft")

        self.initial_balance -= amount

        self.mutex.release()

        return amount
    
    def deposit(self, amount: int) -> int:
        self.mutex.acquire(blocking=True)
        self.initial_balance += amount
        self.mutex.release()
        return amount

accounts: List[BankAccount] = list()
threads: List[Thread] = list()

max_accounts = random.randint(10, 100)

for i in range(max_accounts):
    accounts.append(BankAccount(random.randint(5, 500)))

for i in range(max_accounts):
    account: BankAccount = accounts[i]
    
    for x in range(0, random.randint(4, 20)):
        def thread_func(function, int, bool): 
            try:
                function_name = "Withdrawing" if bool else "Depositing"
                function(int)
                print(f"{function_name} {int} dollars")
            except Exception as over_draft:
                print(over_draft)

        withdrawl = x % 2 == 0
        function = account.withdraw if x % 2 == 0 else account.deposit
        thread = Thread(target=thread_func, args=[function, random.randint(0, 750), withdrawl])
        thread.start()
        threads.append(thread)


for thread in threads:
    thread.join()