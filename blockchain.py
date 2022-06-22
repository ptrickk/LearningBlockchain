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


class Blockchain:

    def __init__(self, difficulty, miningReward):
        self.miningReward = miningReward
        self.difficulty = difficulty
        self.chain = []
        self.pending = []
        self.__createGenesisBlock()

    def __createGenesisBlock(self) -> None:
        block = Block([], '0000000000000000000000000000000000000000000000000000000000000000')
        self.chain.append(block)

    def createTransaction(self, transaction):
        self.pending.append(transaction)

    def minePendingTransactions(self, minerAdress):
        block = Block(self.pending, self.chain[(len(self.chain) - 1)].hash)
        block.mineBlock(self.difficulty)

        self.chain.append(block)
        self.pending = [Transaction(None, minerAdress, self.miningReward)]

    def getAdressBalance(self, address) -> float:
        balance = 0
        for b in self.chain:
            for t in b.transactions:
                if t.fromAddress == address:
                    balance -= t.amount
                elif t.toAddress == address:
                    balance += t.amount
        return balance

    def printChain(self):
        for i, obj in enumerate(self.chain):
            print(f'Block {i} SHA digest: {obj.hash}')
