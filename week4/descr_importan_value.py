class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        pass

    def __set__(self, obj, value):
        with open('log', 'w') as f:
            f.write(str(value))

        self.amount = value

class Account:
    amount = ImportantValue(100)


bobs_account = Account()

bobs_account.amount = 150

with open('log') as f:
        print(f.read())
