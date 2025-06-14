from groupChat import GroupChat
from user import User
from message import message

class ChatServer:
    _instance = None
    def __init__(self) -> None:
        self.users = dict()
        self.groups = dict()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def registerUser(self,user:User):
        self.users[user.getUsername()]=user

    def getUsers(self):
        return self.users

    def registerGroup(self,group:GroupChat):
        self.groups[group.getGroupName]=group

    def sendMessage(self,message:message):
        if(isinstance(message.receiver,User)):   # 1-1 message
            message.receiver.receiveMessage(message)
        elif(isinstance(message.receiver,GroupChat)): # group Message
            message.receiver.broadcastMessage(message)
