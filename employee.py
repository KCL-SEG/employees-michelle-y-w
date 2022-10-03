"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Contract:
    def __init__(self, fixed_rate, hour, hour_rate):
        self.fixed_rate = fixed_rate
        self.hour = hour_rate
        self.hour_rate = hour_rate

    def pay(fixed_rate, hour, hour_rate):
        if self.fixed_rate:
            return self.fixed_rate
        else:
            return self.hour * self.hour_rate

class Commission:
    def __init__(self, bonus, contract_no, contract_rate):
        self.bonus = bonus
        self.contract_no = contract_no
        self.contract_rate = contract_rate
    def pay(bonus, contract_no, contract_rate):
        if self.bonus:
            return self.bonus
        else:
            return self.contract_no * self.contract_rate

class Employee:
    def __init__(self, name):
        self.name = name
        self.fixed_rate = 0
        self.hour = 0
        self.hour_rate = 0
        self.bonus = 0
        self.contract_no = 0
        self.contract_rate = 0

    def basic(self):
        return Contract().pay(self.fixed_rate, self.hour, self.hour_rate)

    def commission(self):
        return Commission().pay(self.bonus, self.contract_no, self.contract_rate)

    def get_pay(self):
        return basic(self) + commission(self)

    def __str__(self):
        #return self.name
        if self.fixed_rate and not self.bonus and not self.contract_rate:
            return(f'{self.name} works on a monthly salary of {basic(self)}.  Their total pay is {get_pay(self)}.')
        if self.fixed_rate and self.bonus:
            print(f'{self.name} works on a monthly salary of {basic(self)} and receives a commission for {self.contract_no} contract(s) at {self.contract_rate}/contract.  Their total pay is {get_pay(self)}.')
        if self.fixed_rate and not self.bonus:
            print(f'{self.name} works on a monthly salary of {basic(self)} and receives a bonus commission of {self.bonus}.  Their total pay is {get_pay(self)}.')

        if not self.fixed_rate and not self.bonus and not self.contract_rate:
            print(f'{self.name} works on a contract of {self.hour} hours at {self.hour_rate}/hour.  Their total pay is {get_pay(self)}.')
        if not self.fixed_rate and not self.bonus:
            print(f'{self.name} works on a contract of {self.hour} hours at {self.hour_rate}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {get_pay(self)}.')
        if not self.fixed_rate and self.bonus:
            print(f'{self.name} works on a contract of {self.hour} hours at {self.hour_rate}/hour and receives a commission for {self.contract_no} contract(s) at {self.contract_rate}/contract.  Their total pay is {get_pay(self)}.')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
