import User
class UserManager:
    user_arr = []
    def __init__(self,filename):
       f = open(filename, "a")
       import csv

       with open("UserMappings.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                user_arr.append(User(row[0],row[1],row[2],row[3]))
    
    def GetUserArray(self):
        return user_arr

    def GetUser(self,UserID,user_arr):
        for user in user_arr:
            if user.UserID == UserID:
                return user