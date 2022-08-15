class User:
    def __init__(self,UserID,Name,Pronouns,ADMIN_PRIV):
        self.UserID = UserID
        self.Name = Name
        self.Pronouns = Pronouns
        if ADMIN_PRIV == 'ADMIN':
            self.ADMIN_PRIV = True
        else:
            self.ADMIN_PRIV = False