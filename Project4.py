class Customer:
    def __init__(self, name, DOB, address, SSN, duration, account_number, balance = 0.0):
        self.name = name
        self.DOB = DOB
        self.address = address
        self.SSN = SSN
        #duration is how long a customer has been with the bank
        self.duration = duration
        self.account_number = account_number
        self.balance = balance
        self.deleted = False
    '''
    Bob=Customer('Bob','11/05/67', '123 Street Ave', '123-45-678', '5','43455463532',5000)
    '''
    def deposit(self, amount):
        if self.deleted == True:
            return ("This account has been closed")
        else:        
            self.balance += amount
            return self.balance
    '''
    Bob.deposit(500) >>> 5500
    '''

    def withdraw(self, amount):
        if self.deleted == True:
            return ("This account has been closed")
        else:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else: 
                return("The withdraw has been stopped due to overdraft protection")
    '''
    Bob.withdraw(1500) >>> 4000
    Bob.withdraw(600000) >>> The withdraw has been stopped due to overdraft protection
    '''
    def checkBalance(self):
        if self.deleted == True:
            return ("This account has been closed")
        else:
            return 'Your balance is {}'.format(self.balance)
    '''
    Bob.checkBalance() >>> Your balance is 4000
    '''

class Employee(Customer):
    def __init__(self, emp_name, position, years):
        self.emp_name = emp_name
        self.position = position
        #years is the number of years spent working at the bank
        self.years = years
        #If the Employee is created only using the Employee class it will only gain access to the basic Employee commands and not specific ones from below
    '''
    Jim=Employee(Jim,Teller,'6') 
    '''
    def employeeInfo(self):
        return '{} has been a {} for {} years'.format(self.emp_name, self.position, self.years)
    '''
    Jim.employeeInfo() >>> Jim has been a Teller for 6 years
    '''
    def getBalance(self, other):
        if other.deleted == True:
            return "This account has been closed"
        else:
            return '{} has balance of {}'.format(other.name, other.balance)
    '''
    Jim.getBalance(Bob) >>> Bob has balance of 4000
    '''

class Manager(Employee):
    def __init__(self, emp_name, position, years, officeNumber):
        Employee.__init__(self, emp_name, position, years)
        self.officeNumber = officeNumber
    
    def findOffice(self):
        return "{}'s office is office number {}".format(self.emp_name, self.officeNumber)
    
    def getInfo(self, other):
        if other.deleted == True:
            return ("{} has been a customer for {} years. " + "Account Number: {} has a balance of $0. " + "SSN: {} " + "Address: {}." + "This account has been closed by a manager.").format(other.name, other.duration, other.account_number, other.SSN, other.address)
        else:
            return ("{} has been a customer for {} years. " + "Account Number: {} has a balance of ${}. " + "SSN: {} " + "Address: {}").format(other.name, other.duration, other.account_number, other.balance, other.SSN, other.address)

    def deleteAccount(self, other):
        if other.deleted == True:
            return ("This account has been closed")
        else:
            other.deleted = True

class Assistant(Employee):
    def __init__(self, emp_name, position, years, supervisor):
        Employee.__init__(self, emp_name, position, years)
        self.supervisor = supervisor
    
    def giveSupervisor(self):
        return "{}'s supervisor is {}".format(self.emp_name, self.supervisor)
   
    def getInfo(self, other):
        if other.deleted == True:
            return ("{} has been a customer for {} years. " + "Account Number: {} has a balance of $0. This account has been closed by a manager.").format(other.name, other.duration, other.account_number)
        else:
            return ("{} has been a customer for {} years. " + "Account Number: {} has a balance of ${}.").format(other.name, other.duration, other.account_number, other.balance)

    def giveLoan(self, other, amount, interest, months):
        payment = (amount*interest) + amount
        monthly_payment = payment/months
        monthly_payment = round(monthly_payment, 2)
        return "{} is requesting a ${} loan. The loan will be paid off by ${} per month for {} months.".format(other.name, amount, monthly_payment, months)


class Teller(Employee):
    def __init__(self, emp_name, position, years, window_number):
        Employee.__init__(self, emp_name, position, years)
        self.window_number = window_number
    
    def giveWindow(self):
        return "{}'s window number is is {}".format(self.emp_name, self.winow_number)
    
    def getInfo(self, other):
        if other.deleted == True:
            return ("Account Number: {} has a balance of $0. This account has been closed by a manager").format(other.account_number)
        else:
            return ("Account Number: {} has a balance of ${}.").format(other.account_number, other.balance)
