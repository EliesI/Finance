# src/finance/finance.py
import json

CHARGES_PERCENTAGE = 0.45
LEISURE_PERCENTAGE = 0.25
INVESTMENT_PERCENTAGE = 0.10
DONATIONS_PERCENTAGE = 0.03
SAVINGS_PERCENTAGE = 0.15
UNFORESEEN_EXPENSES_PERCENTAGE = 0.02

class Account:
    def __init__(self, salary):
        self.charges = salary * CHARGES_PERCENTAGE
        self.leisure = salary * LEISURE_PERCENTAGE
        self.investment = salary * INVESTMENT_PERCENTAGE
        self.donations = salary * DONATIONS_PERCENTAGE
        self.savings = salary * SAVINGS_PERCENTAGE
        self.unforeseen_expenses = salary * UNFORESEEN_EXPENSES_PERCENTAGE
        self.total = self.charges + self.leisure + self.investment + self.donations + self.savings + self.unforeseen_expenses
        self.expenses = []
        self.history = []

    def reset(self, salary):
        self.charges = salary * CHARGES_PERCENTAGE
        self.leisure = salary * LEISURE_PERCENTAGE
        self.investment = salary * INVESTMENT_PERCENTAGE
        self.donations = salary * DONATIONS_PERCENTAGE
        self.savings = salary * SAVINGS_PERCENTAGE
        self.unforeseen_expenses = salary * UNFORESEEN_EXPENSES_PERCENTAGE
        self.total = self.charges + self.leisure + self.investment + self.donations + self.savings + self.unforeseen_expenses

    def update_total(self):
        self.total = self.charges + self.leisure + self.savings + self.donations + self.unforeseen_expenses + self.investment

    def add_expense(self, type, price, desc):
        if type == "charges":
            self.charges -= price
        elif type == "leisure":
            self.leisure -= price
        elif type == "investment":
            self.investment -= price
        elif type == "donations":
            self.donations -= price
        elif type == "savings":
            self.savings -= price
        elif type == "unforeseen_expenses":
            self.unforeseen_expenses -= price
        else:
            return "Invalid type"
        
        self.expenses.append({"Type": type, "Price": price, "Description": desc})
        self.update_total()

    def to_json(self):
        return json.dumps({"Charges": self.charges, "Donations": self.donations, "Savings": self.savings, 
                           "Unforeseen Expenses": self.unforeseen_expenses, "Investment": self.investment, 
                           "Leisure": self.leisure, "Total": self.total}, indent=4, sort_keys=True)
    
    def json_expenses(self):
        return json.dumps({"Expenses": self.expenses}, indent=4, sort_keys=True)
    
    def json_history(self):
        return json.dumps({"History": self.history}, indent=4, sort_keys=True)

    def save_month(self, month, salary):
        self.history.append({"Month" : month, "Account" : {"Charges": self.charges, "Donations": self.donations, "Savings": self.savings, 
                           "Unforeseen Expenses": self.unforeseen_expenses, "Investment": self.investment, 
                           "Leisure": self.leisure, "Total": self.total}, "Expenses": self.expenses })
        self.reset(salary)
