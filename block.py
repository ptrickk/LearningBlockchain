import hashlib
from transaction import Transaction

class Block:

    def __init__(self, transactions: Transaction, previous):
        self.transactions = transactions
        self.previous = previous
        self.nonce = 0
        self.calculateHash()

    def calculateHash(self):
        raw = str(self.transactions) + "/" + str(self.previous) + "/" + str(self.nonce)
        encoded = raw.encode('utf-8')
        self.hash = hashlib.sha256(encoded).hexdigest()

    def mineBlock(self, difficulty):
        while not self.hash[0:difficulty].__eq__('0' * difficulty):
            self.nonce += 1
            self.calculateHash()

        print(f'BLOCK MINED: {self.hash}')

    def Hash(self) -> str:
        return hash

    def hasValidTransaction(self):
        for t in self.transactions:
            if not t.isValid():
                return False
        return True