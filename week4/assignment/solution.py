import tempfile
import uuid
import os

class File:
    def __init__(self, name):

        if name == '':
            raise EmptyFilename

        self.name = os.path.join(os.getcwd(), name)
        self.content = ''

        try:
            with open(name, 'r') as f:
                self.content = f.read()


        except FileNotFoundError:
            with open(name, 'w') as f:
                f.write( self.content )

        self.f = open(self.name, 'r')

    def __exit__(self):
        self.f.close()
            
    def __iter__(self):
        return self

    def __next__(self):
        try:
            line = self.f.readline()
            if line == '':
                raise StopIteration

        except:
            self.f.close()
            raise StopIteration

        return line

    def __str__(self):
        return self.name

    def read(self):
        return self.content

    def write(self, content):
        self.content = content

        with open(self.name, 'w') as f:
            f.write( self.content )

        return len(self.content)

    def __add__(self, obj):
        if not isinstance(obj, File):
            raise TypeError

        wd = tempfile.gettempdir()
        filename = os.path.join( wd, str(uuid.uuid4()) )

        content = self.content + obj.content

        file_new = File(filename)
        file_new.write(content)

        return file_new

myfile = File('notfound')
myfile.write("The world is mine!")

print(myfile.read())
print(myfile)

file_a = File('file_a')
file_b = File('file_b')

file_a.write('line a\n')
file_b.write('line b\n')

file_c = file_a + file_b

print(file_c)
#print(file_c.read())

for line in file_c:
    print(ascii(line))



