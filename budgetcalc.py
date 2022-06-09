class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.balance = 0
        self.total_spend = float()
        self.percentage_total = 0
        self.percent_points = []

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": round(float(amount),2), "description": description})
        self.balance = self.balance + amount


    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -1 * round(float(amount),2), "description": description})
            self.balance = self.balance - amount
            self.total_spend = self.total_spend + amount
            return True
        else:
            return False
    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_cat):
        if self.check_funds(amount) is True:
            self.withdraw(amount, "Transfer to " + target_cat.category)
            target_cat.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return  False

    def check_funds(self, amount):
        check_amount = amount
        if self.balance >= check_amount:
            return True
        else:
            return False
    def round_to_ten(self,number):
        if number < 10:
            return 0
        else:
            return  int(number)

    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total



    def __str__(self):
        ledger_print = """"""
        for entry in self.ledger:
            ledger_print += str(entry["description"][:23]).ljust(23) + str(format(entry["amount"], '.2f')).rjust(7) + "\n"

        return  (str(self.category).center(30,"*") + "\n" + ledger_print + 'Total: ' + str(self.balance))


def total_spend(categories):
    all_total_spend = float()
    # work out total spend
    for category in categories:
        cat_spend = category.get_withdrawals()
        all_total_spend = all_total_spend + cat_spend
    return all_total_spend

def cat_percent(categories, all_total_spend):
    # % total spend for each category
    percent_by_cat = []
    for category in categories:
        category.percentage_total = (-1 * (category.total_spend / all_total_spend)) * 100
        category.percent_points = int(category.percentage_total)
        percent_by_cat.append(category.percent_points)

    return percent_by_cat


def create_spend_chart(cats):

    # works out longest name
    name_length = 0
    for category in cats:
        if len(category.category) > name_length:
            name_length = len(category.category)

    # setting up output string dimensions
    output = ""
    num_cats = 0
    spaces = 7
    for category in cats:
        num_cats +=1
        spaces += 2

    # calculate no of dashes
    dashes = ("-" * (spaces-4)).rjust(spaces)

    # calculates total spend and percentage per category, puts percentages into dictionary
    all_total_spend = total_spend(cats)
    percent_by_cat = cat_percent(cats, all_total_spend)

    #adds bars to output string
    y_axis = 100
    cat_spaces = str()
    filler = str()
    output_line = ""
    while y_axis > -1:
        filler = list()
        lister_iter = 0
        for x in percent_by_cat:
            if x >= y_axis:
                filler.append('{}'.format("o  "))
            else:
                filler.append('{}'.format("   "))
        lister_iter += 1
        filler_str = "".join(filler)
        output += str(y_axis).rjust(3) + "| " + filler_str + "\n"
        y_axis -= 10
    

    output += dashes



    return output

