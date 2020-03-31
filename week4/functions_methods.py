class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def full_name(self):
        return "{} {}".format(self.fname, self.lname)


amy = User('Amy', 'Jones')

print(amy.fname)
print(User.full_name)
