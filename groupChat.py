from generateID import generateID
from message import message
from user import User

class GroupChat:
    def __init__(self,name:str,admin:User):
        self.groupName = name
        self.groupId = generateID()
        self.admin = admin
        self.members = set()
        self.members.add(self.admin) #adding admin to group

    def getGroupId(self):
        return self.groupId

    def getGroupName(self):
        return self.groupName
    
    def addMember(self,requestedBy:User,user:User):
        if requestedBy.getUserId() != self.admin.getUserId():
            print("only admin has this priviligue")
        else:
            self.members.add(user)
            user.groups.add(self.groupName)

    def removeMember(self,requestedBy:User,user:User):
        if requestedBy.getUserId() != self.admin.getUserId():
            print("only admin has this priviligue")
        else:
            self.members.remove(user)
            user.groups.remove(self.groupName)

    def getMembers(self):
        members = []
        for i in self.members:
            members.append(i.getUsername())
        return members
    
    def broadcastMessage(self,message:message):
        for user in self.members:
            if(user.getUserId() != self.admin.getUserId()):
                user.receiveMessage(message)

