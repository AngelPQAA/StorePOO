class Distributor:

    def __init__(self, enterprise, debt, pbx):
        self.enterprise = enterprise
        self.debt = debt
        self.pbx = pbx

    def view(self):
        print(f'enterprise: {self.enterprise} \ndebt: {self.debt} \npbx: {self.pbx}')
