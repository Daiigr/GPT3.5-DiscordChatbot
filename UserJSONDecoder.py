import json
from User import User

class UserDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        return User(dct['UserID'], dct['Name'], dct['Pronouns'], dct['ADMIN_PRIV'])