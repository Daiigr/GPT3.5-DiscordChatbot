
import User
class UserSearcher:
    """
    this class contains the functions to quickly search the user array for certain parameters
    """
    # this function sorts a array of users by their name
    def sortUsersByName(self, user_array):
        user_array.sort(key=lambda x: x.Name)
        return user_array
    
    # this function sorts a array of users by their ID
    def sortUsersByID(self, user_array):
        user_array.sort(key=lambda x: x.UserID)
        return user_array
    
    # this function sorts a array of users by their pronouns
    def sortUsersByPronouns(self, user_array):
        user_array.sort(key=lambda x: x.Pronouns)
        return user_array
    
    def getUserByIDWithBinarySearch(self, user_array, UserID):
        """
        this function returns a user object from a array of users based on the user ID using a binary search
        """
        user_array = self.sortUsersByID(user_array)
        low = 0
        high = len(user_array) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if user_array[mid].UserID < UserID:
                low = mid + 1
            elif user_array[mid].UserID > UserID:
                high = mid - 1
            else:
                return user_array[mid]
        return None
