class Contact:
    def __init__(self,name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone

    def __str__(self):
        return f"Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone}"

    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email
    
    def getPhone(self):
        return self.__phone
    
    def setName(self, name):
        self.__name = name

    def setEmail(self, email):
        self.__email = email
        
    def setPhone(self, phone):
        self.__phone = phone
    
    