class User:
    def __init__(self,UserID,Name,Pronouns,ADMIN_PRIV):

        """
        object representing a discord user
        Parameters:
        UserID: The ID of the user
        Name: The name of the user
        Pronouns: The pronouns of the user
        ADMIN_PRIV: The admin privilages of the user
        Methods:
        get_name: returns the name of the user

        """
        self.UserID = UserID
        self.Name = Name
        self.Pronouns = Pronouns
        if ADMIN_PRIV == 'ADMIN':
            self.ADMIN_PRIV = True
        else:
            self.ADMIN_PRIV = False
    
    def get_name(self):
        return self.Name