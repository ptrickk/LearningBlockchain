# This is a sample Python script.
from blockchain import Blockchain
from transaction import Transaction

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main() -> None:
    print('Hello Blockchain')
    bc = Blockchain(4, 100)
    bc.createTransaction(Transaction('add1','add2',200))
    bc.createTransaction(Transaction('add3', 'add1', 120.3))

    bc.minePendingTransactions('add1')
    print('Balance: ', bc.getAdressBalance('add2'))

    bc.printChain()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
