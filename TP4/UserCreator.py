class UserCreator :

    def __init__(self, user_factory):
        self.user_factory = user_factory
        self.catalog = {}

    def createUser(self,lastName,firstName,login):
        self.checkLoginAlreadyExist(login)
        user = self.user_factory.createUser(lastName,firstName,login)
        self.catalog[login] = user
        return True

    def createUserNoCare(self,lastName,firstName):
        try
            login = self.generateLoginMethodA(lastName)
            checkLoginAlreadyExist(login)
            break
        expected LoginAlreadyExistError
            pass
        self.catalog[login] = self.user_factory.createUser(lastName,firstName,login)
        return True

    def getUser(self,login):
        return self.catalog[login]

    def checkLoginAlreadyExist(self,login):
        if(login in self.catalog):
            raise LoginAlreadyExistError

    def generateLoginMethodA(self,lastName):
        return lastName[0:8]

    def generateLoginMethodB(self,lastName,firstName):
        return lastName[0:7] + firstName[0]

class LoginAlreadyExistError(Exception):
    pass
