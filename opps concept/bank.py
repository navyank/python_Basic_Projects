class BankAccount:
    def __init__(self,account_number,principle):
        self.account_number=account_number
        self.principle=principle
class SavingsAccount(BankAccount):
    def __init__(self,principle,account_number):
        BankAccount.__init__(self,account_number,principle)
    def calculate_interest(self,rate,time):
        self.rate=rate
        self.time=time
        self.interest=self.principle*self.rate*self.time/100
        print(self.interest)
o=SavingsAccount(230000,1000)
o.calculate_interest(0.5,2)

                