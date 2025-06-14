from generateID import generateID
from enum_1 import messageStatus

class User:
    groups=set()
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
    
    def updateGroups(self,group):
        User.groups.add(group.getGroupName())
    
    def getGroups(self):
        return User.groups
    
    def receiveMessage(self,message):
        message.messageStatus=messageStatus.SENT
        print(message.sender.name + ' sent '+ message.getContent() + " to "+self.name)
        message.messageStatus=messageStatus.SEEN