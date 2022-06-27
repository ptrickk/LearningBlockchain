from block import Block
from transaction import Transaction

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

    def addTransaction(self, transaction):
        if transaction.isValid():
            print('VALID TX')
            self.pending.append(transaction)
        else:
            raise Exception('Transaction has invalid signature!')

    def minePendingTransactions(self, minerAdress):
        block = Block(self.pending, self.chain[(len(self.chain) - 1)].hash)
        block.mineBlock(self.difficulty)

        self.chain.append(block)
        t = Transaction(None, minerAdress, self.miningReward)
        self.pending = [t]

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

    def Validate(self) -> bool:
        for i, obj in enumerate(self.chain):
            if i > 0:
                prev = self.chain[i-1]
                if not obj.previous == prev.hash:
                    return False
                if not obj.hasValidTransaction():
                    return False
        return True
