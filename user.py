from generateID import generateID
from message import message

class User:
    def __init__(self, name, phone):
        self.name = name
        self.userId = generateID()
        self.phoneNo = phone
        self.isonline = False

    def getUserId(self):
        return self.userId

    def getUsername(self):
        return self.name

    def goOffline(self):
        self.isonline = False

    def goOnline(self):
        self.isonline = True
    
    def isAvailable(self):
        return self.isonline
    
    def receiveMessage(self,message):
        print(message.sender.name,message.getContent(),self.name)

user1=User("mani",9849)
user2=User("raju",7412)
message1=message(user2,user1,"hi")
user1.receiveMessage(message1)