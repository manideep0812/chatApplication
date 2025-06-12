import uuid

def generateID():
    uuid_str = str(uuid.uuid4()).replace('-', '')
    return uuid_str[:8]