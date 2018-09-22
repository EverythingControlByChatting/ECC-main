class BaseRequest(dict):
    
    def __init__(self, platfrom, text, user_name, user_id):
        super().__init__(self)
        self['platfrom'] = platfrom
        self['text'] = text
        self['user_name'] = user_name
        self['user_id'] = user_id


def getDict(dic, key):
    if (key in dic):
        return dic[key]
    else:
        return None
