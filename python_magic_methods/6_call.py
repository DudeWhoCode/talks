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
        if self.balance < 0:
            raise ValueError('sorry cannot go in debt!')

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

    def __call__(self):
        print('Account owner: {}'.format(self.owner))
        print('Account Balance: {}'.format(self.balance))
        print('Last 5 transactions: {}'.format(self._transactions[:5]))


if __name__ == '__main__':
    franks_ledger = Ledger('Frank')
    franks_ledger.add_transaction(50)
    franks_ledger.add_transaction(200)
    franks_ledger.add_transaction(30)
    franks_ledger.add_transaction(500)
    franks_ledger.add_transaction(900)
    franks_ledger.add_transaction(-70)

    franks_ledger()
