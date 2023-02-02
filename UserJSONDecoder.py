import json
from User import User

class UserDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        return User(dct['UserID'], dct['Name'], dct['Pronouns'], dct['ADMIN_PRIV'])

user_json = '{"UserID": 123, "Name": "John Doe", "Pronouns": "he/him", "ADMIN_PRIV": "ADMIN"}'
user = json.loads(user_json, cls=UserDecoder)
print(user.__dict__)
