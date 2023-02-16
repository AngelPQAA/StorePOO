class Client:

    def __init__(self, id, total_purchases, total_discount):
        self.id = id
        self.total_purchases = total_purchases
        self.total_discount = total_discount

    def view(self):
        print(f'id: {self.id} \ntotal_purchases: {self.total_purchases} \ntotal_discount: {self.total_discount}')