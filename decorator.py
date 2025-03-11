class Employee:
    def __init__(self):
        self.income = 0 

    def earn_income(self, money):
        self.income += money
    @property
    def tax_amount(self):
        return self.income * 0.05
    
    @tax_amount.setter
    def tax_amount(self,tax_number ):
        self.income += tax_number*20
    
wilson = Employee()
# wilson.earn_income(500)
print (wilson.tax_amount) #tax amount is not a real property
#tax amount virtual property is read-only
wilson.tax_amount = 200
print(wilson.income)



def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before the original function")
        original_func()
        print("Some extra code after the original function")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()
