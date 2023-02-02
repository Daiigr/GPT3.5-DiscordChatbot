#this class adds, creates and deletes user objects from a json file through the methods AddUserToJson, RemoveUserFromJson,GetUserFromJson which returns a user object
import json
import User
import os

from UserJSONDecoder import UserDecoder
from UserJSONEncoder import UserEncoder

class UserJsonParser:
        """
        this class adds, creates and deletes user objects from a json file through the methods AddUserToJson, RemoveUserFromJson,GetUserFromJson which returns a user object
        """

        def __init__(self):
                """
                this class adds, creates and deletes user objects from a json file through the methods AddUserToJson, RemoveUserFromJson,GetUserFromJson which returns a user object
               
                constructor for the UserJsonParser class checks if the json file exists and if it does it loads the user list from the json file
                """

                self.json_file_path = os.path.join(os.path.dirname(__file__), 'users.json')
                if os.path.exists(self.json_file_path):
                        self.user_list = self.GetUserListFromJson()
                else:
                        self.user_list = []
                        with open(self.json_file_path, 'w') as json_file:
                                json.dump(self.user_list, json_file)

        def GetUserListFromJson(self):
                """
                this method returns a list of user objects from a json file
                """
                with open(self.json_file_path, 'r') as json_file:
                        user_list = json.load(json_file, cls=UserDecoder)
                return user_list

        def SaveUserListToJson(self):
                """
                this method saves a list of user objects to a json file
                """
                with open(self.json_file_path, 'w') as json_file:
                        json.dump(self.user_list, json_file, cls=UserEncoder)
            
        

        def AddUser(self, user):

                """
                this method adds a user object to a json file
                Overwrites the user if the user already exists

                """
                if self.getUserByID(user.UserID) is not None:
                        self.RemoveUserByID(user.UserID)
                self.user_list.append(user)
                self.SaveUserListToJson()
            
        def RemoveUser(self, User):

                """
                this method removes a user object from a json file
                """

                try:
                    self.user_list.remove(User)
                except ValueError:
                    print("User not found")
                self.SaveUserListToJson()

        def RemoveUserByID(self, user_id):
                """
                this method removes a user object from a json file
                """
                user = self.getUserByID(user_id)
                if user is not None:
                        self.RemoveUser(user)
                else:
                        print("User not found")
                self.SaveUserListToJson()


        def getUserByID(self, user_id):
                """
                this method returns a user object from a json file
                """

                for user in self.user_list:
                        if user.UserID == user_id:
                                return user
                return None

        def getUserByName(self, user_name):
                """
                this method returns a user object from a json file
                """
                for user in self.user_list:
                        if user.Name == user_name:
                                return user
                return None

        def getUserFromJsonByPronouns(self, user_pronouns):
                """
                this method returns a user object from a json file
                """
                for user in self.user_list:
                        if user.Pronouns == user_pronouns:
                                return user
                return None