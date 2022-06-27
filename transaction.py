import hashlib
import rsa

class Transaction:
    
    def __init__(self, fromAddress, toAddress, amount):
        self.amount = amount
        self.toAddress = toAddress
        self.fromAddress = fromAddress

    #Is used as fingerprint
    def calculateHash(self):
        return hashlib.sha256(hex(self.fromAddress.n).encode() + hex(self.toAddress.n).encode() + str(self.amount).encode()).hexdigest()

    def signTransaction(self, keyPair):
        if not keyPair.publicKey == self.fromAddress:
            raise Exception('You can only sign your own transactions!')

        hashTx = self.calculateHash()
        self.sig = rsa.sign(hashTx.encode(), keyPair.privateKey, 'SHA-1')

    def isValid(self) -> bool:
        if self.fromAddress == None:
            return True
        if not self.sig or len(self.sig) == 0:
            raise Exception('Transaction has no signature!')
            return False;

        if rsa.verify(self.calculateHash().encode(), self.sig, self.fromAddress) == 'SHA-1':
            return True
        else:
            return False