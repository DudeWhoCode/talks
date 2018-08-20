from functools import total_ordering


@total_ordering
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

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.balance)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.balance)

    def __getitem__(self, i):
        return self._transactions[i]

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance


if __name__ == '__main__':
    franks_ledger = Ledger('Frank')
    franks_ledger.add_transaction(50)
    franks_ledger.add_transaction(20)
    franks_ledger.add_transaction(-10)

    joes_ledger = Ledger('Joe')
    joes_ledger.add_transaction(50)
    joes_ledger.add_transaction(40)
    joes_ledger.add_transaction(100)

    print(franks_ledger)
    print(joes_ledger)

    print('Has Frank got more money than Joe? :', franks_ledger > joes_ledger)
