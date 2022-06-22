
class Transaction:
    
    def __init__(self, fromAddress, toAddress, amount):
        self.amount = amount
        self.toAddress = toAddress
        self.fromAddress = fromAddress