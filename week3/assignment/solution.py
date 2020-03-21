class FileReader:
    """Класс FileReader помогает читать из файла"""

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path) as f:
                return f.read()
        except IOError:
            return ""

reader = FileReader("not exist")
print( reader.read() )
reader = FileReader('solution.py')
print( reader.read() )
