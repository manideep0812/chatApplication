from generateID import generateID
from message import message
from user import User

class GroupChat:
    def __init__(self,name,admin):
        self.groupName = name
        self.groupId = generateID()
        self.admin = admin
        self.members = set()

    def getGroupId(self):
        return self.groupId

    def getGroupName(self):
        return self.groupName
    
    def addMember(self,requestedBy,user):
        if requestedBy.getUserId() != self.admin.getUserId():
            print("only admin has this priviligue")
        else:
            self.members.add(user)

    def removeMember(self,requestedBy,user):
        if requestedBy.getUserId() != self.admin.getUserId():
            print("only admin has this priviligue")
        else:
            self.members.remove(user)

    def getMembers(self):
        return self.members
    
    def broadcastMessage(self,content):
        for user in self.members:
            user.receiveMessage(message(self.admin,user,content))

