class Data :
    def __init__(self) :
        self.countries = [
            {
                "name" : "India",
                "short" : "In",
                "code" : "+91"
            },
            {
                "name" : "nepal",
                "short" : "np",
                "code" : "+977"
            },
            {
                "name" : "pakistan",
                "short" : "pk",
                "code" : "+92"
            },           
        ]
        print(self.countries)

class Main(Data) :
    def __init__(self) :
        super().__init__()
        print("Hello from main class")

Main()