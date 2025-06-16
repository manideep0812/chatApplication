from chatserver import ChatServer
from groupChat import GroupChat
from message import message
from messageDecorator import ReactionDecorator
from onlineStatus import OnlineStatusChange
from user import User

user1=User("mani",949)
user2=User("raju",123)
user3=User("ravi",852)
user4=User("vamsi",963)
a=ChatServer()
a.registerUser(user1)
a.registerUser(user2)
m1=message(user1,user2,"hi")
a.sendMessage(m1)
# group1=GroupChat("school",user1)
# group1.addMember(user1,user2)
# group1.addMember(user1,user3)
group2=GroupChat("college",user1)
group2.addMember(user1,user2)
group2.addMember(user1,user3)
group2.addMember(user1,user4)
print(group2.getMembers())
#print(user2.getGroups())
# Assuming you want to decorate the message m1 with reactions
print("-------------------")
reactiondecorator = ReactionDecorator(m1)
reactiondecorator.addReaction(user1.getUserId(),"😊")
reactiondecorator.addReaction(user2.getUserId(),"👌")
reactiondecorator.addReaction(user3.getUserId(),"👌")
print(reactiondecorator.getContent())
notification = OnlineStatusChange()
notification.addObserver(user2)
notification.addObserver(user3)
user1.goOffline()
m2=message(user2,group2,"how are you")
a.sendMessage(m2)
