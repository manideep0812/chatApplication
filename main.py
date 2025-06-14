from chatserver import ChatServer
from groupChat import GroupChat
from message import message
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
group1=GroupChat("school",user1)
group1.addMember(user1,user2)
group1.addMember(user1,user3)
group1=GroupChat("college",user1)
group1.addMember(user1,user2)
group1.addMember(user1,user4)
print(user2.getGroups())

