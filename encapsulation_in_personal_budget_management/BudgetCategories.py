class BudgetCategory:
    # Constructor and private attributes
    def __init__(self,category_name,allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    # Getters and setters for category name and budget
    def get_category_name(self):
        return self.__category_name
    def set_category_name(self,new_variable):
        if new_variable == "":
            print("Category name was empty!")
        else:
            self.__category_name=new_variable
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    def set_allocated_budget(self,new_variable):
        if new_variable >= 0:
            self.__allocated_budget=new_variable
        else:
            print("Allocated Budget was not a positive number!\nProgram will default to previously amount.")
    

    def add_expense(self, amount):
        # Method to add an expense to the category
        if amount > self.__allocated_budget:
            print (f"This ${amount} expense exceeds the remaining budgeted amount!\nYou should not make the purchase!")
        else:
            self.set_allocated_budget(self.__allocated_budget-amount)
            print(f"A ${amount} expense was deducted from your remaining budget!")

    def display_category_summary(self):
        # Method to display the budget category details
        print(f"{self.get_category_name()} budget has ${self.get_allocated_budget()} remaining!")
