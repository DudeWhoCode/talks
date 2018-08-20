class Ledger(object):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self._transactions = []

    def add_transaction(self, amount):
        self._transactions.append(amount)
        self.balance += amount

    def __len__(self):
        return len(self._transactions)


if __name__ == '__main__':
    franks_ledger = Ledger('Frank')
    franks_ledger.add_transaction(50)
    franks_ledger.add_transaction(20)
    franks_ledger.add_transaction(-10)

    print(len(franks_ledger))

