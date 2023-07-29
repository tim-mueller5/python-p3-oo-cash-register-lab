#!/usr/bin/env python3

# import ipdb

class CashRegister:
    
    

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = []

    def add_item(self, title, price, quantity=1):
        self.total += (price * quantity)
        for i in range(quantity):
            self.items.append(title)
        self.last_transaction = [title, price, quantity]

    def apply_discount(self):
        if(self.discount):
            self.total = int(self.total - self.total*(self.discount/100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def items(self):
        return self.items
    
    def void_last_transaction(self):
        self.items.pop()
        self.total -= (self.last_transaction[1] * self.last_transaction[2])


    # ipdb.set_trace()