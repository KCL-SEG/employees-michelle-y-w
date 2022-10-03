"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, fixed_pay, salary, work_hour, hour_rate, fixed_commission, bonus, contract_no, contract_rate):
        self.name = name
        self.fixed_pay = fixed_pay
        self.fixed_commission = fixed_commission
        self.salary = salary
        self.work_hour = work_hour
        self.hour_rate = hour_rate
        self.bonus = bonus
        self.contract_no = contract_no
        self.contract_rate = contract_rate
        self.pay = 0
        self.contract_info = ''
        self.commission_info = ''

    def get_name(self):
        return self.name

    def get_pay(self):
        self.contract_pay = 0
        self.commission_pay = 0
        if self.fixed_pay:
            self.contract_pay = SalaryContract(self.contract_pay, self.salary).get_contract_pay()
            self.contract_info = str(f'monthly salary of {self.contract_pay}')

        else :
            self.contract_pay = HourlyContract(self.contract_pay, self.work_hour, self.hour_rate).get_contract_pay()
            self.contract_info = str(f'contract of {self.work_hour} hours at {self.hour_rate}/hour')

        if self.fixed_commission:
            self.commission_pay = BonusCommission(self.commission_pay, self.bonus).get_commission_pay()
            if self.commission_pay:
                self.commission_info = str(f' and receives a bonus commission of {self.commission_pay}. ')
            else :
                self.commission_info = '. '
        else:
            self.commission_pay = ContractCommission(self.commission_pay, self.contract_no, self.contract_rate).get_commission_pay()
            self.commission_info = str(f' and receives a commission for {self.contract_no} contract(s) at {self.contract_rate}/contract. ')

        self.pay = self.contract_pay + self.commission_pay
        return self.pay

    def __str__(self):
        self.intro = str(f'{self.get_name()} works on a {self.contract_info}{self.commission_info} Their total pay is {self.pay}.')
        return self.intro



class Contract():
    def __init__(self, contract_pay):
        self.contract_pay = contract_pay

    def get_contract_pay(self):
        return self.contract_pay

class SalaryContract(Contract):
    def __init__(self, contract_pay, salary):
        Contract.__init__(self, contract_pay)
        self.salary = salary
        self.update_contract_pay()

    def update_contract_pay(self):
        self.contract_pay = self.salary

class HourlyContract(Contract):
    def __init__(self, contract_pay, work_hour, hour_rate):
        Contract.__init__(self, contract_pay)
        self.work_hour = work_hour
        self.hour_rate = hour_rate
        self.update_contract_pay()

    def get_work_hour(self):
        return self.work_hour

    def get_hour_rate(self):
        return self.hour_rate

    def update_contract_pay(self):
        self.contract_pay = self.get_work_hour() * self.get_hour_rate()

class Commission:
    def __init__(self, commission_pay):
        self.commission_pay = commission_pay

    def get_commission_pay(self):
        return self.commission_pay

class BonusCommission(Commission):
    def __init__(self, commission_pay, bonus):
        Commission.__init__(self, commission_pay)
        self.bonus = bonus
        self.update_commission_pay()

    def get_bonus(self):
        return self.bonus

    def update_commission_pay(self):
        self.commission_pay = self.get_bonus()

class ContractCommission(Commission):
    def __init__(self, commission_pay, contract_no, contract_rate):
        Commission.__init__(self, commission_pay)
        self.contract_no = contract_no
        self.contract_rate = contract_rate
        self.update_commission_pay()

    def get_contract_no(self):
        return self.contract_no

    def get_contract_rate(self):
        return self.contract_rate

    def update_commission_pay(self):
        self.commission_pay = self.get_contract_no() * self.get_contract_rate()

# self, name, fixed_pay, salary, work_hour, hour_rate, fixed_commission, bonus, contract_no, contract_rate
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 4000, 0, 0, True, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 0, 100, 25, True, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 3000, 0, 0, False, 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 0, 150, 25, False, 0, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 2000, 0, 0, True, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 0, 120, 30, True, 600, 0, 0)
