import json
from User import User

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                'UserID': obj.UserID,
                'Name': obj.Name,
                'Pronouns': obj.Pronouns,
                'ADMIN_PRIV': obj.ADMIN_PRIV
            }
        return super().default(obj)

user = User(123, "John Doe", "he/him", "ADMIN")
user_json = json.dumps(user, cls=UserEncoder)

print(user_json)