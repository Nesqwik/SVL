
class Compte:

    def __init__(self):
        '''
            >>> c = Compte()
            >>> c.get_balance()
            0
        '''
        self.balance = 0

    def get_balance(self):
        '''
            >>> c = Compte()
            >>> c.get_balance()
            0
        '''
        return self.balance

    def credit(self, amount):
        '''
            >>> c = Compte()
            >>> c.credit(10)
            >>> c.get_balance()
            10
            >>> c.credit(-10)
            Traceback (most recent call last):
            [...]
            ValueError

            >>> c.credit(0)
            Traceback (most recent call last):
            [...]
            ValueError
        '''

        if amount <= 0:
            raise ValueError()
        self.balance += amount

    def debit(self, amount):
        '''
            >>> c = Compte()
            >>> c.credit(10)
            >>> c.debit(10)
            >>> c.get_balance()
            0
            >>> c.debit(1)
            Traceback (most recent call last):
            [...]
            ValueError

            >>> c.debit(-10)
            Traceback (most recent call last):
            [...]
            ValueError

            >>> c.debit(0)
            Traceback (most recent call last):
            [...]
            ValueError
        '''
        if self.balance < amount or amount <= 0:
            raise ValueError()
        self.balance -= amount
