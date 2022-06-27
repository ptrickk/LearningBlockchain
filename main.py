# This is a sample Python script.
from blockchain import Blockchain
from transaction import Transaction
from keygenerator import KeyGenerator
from keygenerator import Key

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main() -> None:
    print('Hello Blockchain')

    kg1 = KeyGenerator(512, 'key1.txt')
    kg2 = KeyGenerator(512, 'key2.txt')
    kg1.generate()
    kg2.generate()
    k1 = Key('key1.txt')
    k2 = Key('key2.txt')

    print(hex(k1.privateKey.n) )
    print(k1.publicKey)

    bc = Blockchain(4, 100)
    t1 = Transaction(k1.publicKey,k2.publicKey,200)
    t1.signTransaction(k1)

    t2 = Transaction(k2.publicKey, k1.publicKey, 120.3)
    t2.signTransaction(k2)

    bc.addTransaction(t1)
    bc.addTransaction(t2)

    bc.minePendingTransactions(k1.publicKey)
    bc.minePendingTransactions(k1.publicKey)
    print('Balance: ', bc.getAdressBalance(k1.publicKey))
    print(bc.Validate())

    bc.printChain()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
