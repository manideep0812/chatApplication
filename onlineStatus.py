class OnlineStatusChange:
    __observers=set()
    #Singleton pattern
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def addObserver(self,user):
        self.__observers.add(user)
    def removeObserver(self,user):
        self.__observers.remove(user)
    def notifyUsers(self,changedUser):
        for i in self.__observers:
            status = "onine" if changedUser.isonline else "offline"
            notification = i.getUsername() + " notified : " + changedUser.getUsername() + " is " + status
            i.getStatusNotification(notification)

