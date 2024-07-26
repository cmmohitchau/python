class Admin : 
    def __init__(self) :
        self.name = "mohit"
        self.username = "@mohit"
        self.__password = "12345" #__ double underscore means making that var private
        
    def getPassword(self) :
        return self.__password
    
    def setPassword(self,data) :
        self.__password = data
        

admin = Admin()

print(admin.name)
admin.setPassword("hellow")
print(admin.getPassword())