from convert import Convert

class Main(Convert) :
    def __init__(self):
        super().__init__()
        print(self.upperCase("mohit"))

main = Main()