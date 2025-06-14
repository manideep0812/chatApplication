from enum_1 import messageStatus
from generateID import generateID
from user import User


class message:
    def __init__(self,sender:User,receiver,content:str):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.messageStatus = messageStatus.DRAFT
        self.messageID = generateID()
    def getContent(self):
        return self.content
    def getMessageId(self):
        return self.messageID
    

    