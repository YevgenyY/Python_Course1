class FileReader:
    _filename = ''

    def __init__(self, name):
        self.setfilename(name)

    @classmethod 
    def setfilename(cls, name):
        cls._filename = name

    @classmethod 
    def getfilename(cls):
        return cls._filename
        

    @staticmethod
    def read():
        try:
            filename = FileReader.getfilename()
            with open(filename) as f:
                result = f.read()

            return result

        except FileNotFoundError:
            return ''

'''
reader = FileReader('testnotexist')
text = reader.read()
reader = FileReader('test.txt')
print(reader.read())
'''
