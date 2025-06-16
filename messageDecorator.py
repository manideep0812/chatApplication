from abc import ABC, abstractmethod
from dataclasses import dataclass
from os import read

#decorator pattern
class ImessageDecorator(ABC):
    @abstractmethod
    def getContent(self)->str:
        pass

class MessageDecorator(ImessageDecorator):
    def __init__(self,baseMessage):
        self.baseMessage = baseMessage
    @abstractmethod
    def getContent(self)->str:
        pass

@dataclass
class ReactionType:
    userid:str
    emoji:str

class ReactionDecorator(MessageDecorator):
    reactions = []
    def addReaction(self,userId:str,emoji:str):
        reaction = ReactionType(userId,emoji)
        if reaction not in self.reactions:
            self.reactions.append(reaction)

    def removeReaction(self,userId:str,emoji:str):
        reaction = ReactionType(userId,emoji)
        if reaction in self.reactions:
            self.reactions.remove(reaction)

    def getReactions(self):
        return self.reactions
    
    def reactionSummary(self):
        reactionsDict = dict()
        for i in self.reactions:
            if i.emoji not in reactionsDict:
                reactionsDict[i.emoji] = 1
            else:
                reactionsDict[i.emoji] += 1
        return reactionsDict
    
    def getContent(self):
        return (self.baseMessage.getContent() + str(self.reactionSummary()))

