import discord

class UserManagementEmbeds:
    def createAddedUserEmbed(DiscordUser, name, pronouns, admin_priv):

        embed = discord.Embed(title="added User", description="User has been added to the system", color=0x00ff00)
        embed.add_field(name="Added User" + str(DiscordUser), value="as " + name + "("+pronouns+")" , inline=False)
        embed.add_field(name="is admin" , value=admin_priv, inline=False)
        return embed
    
    def createRemovedUserEmbed(DiscordUser):
        embed = discord.Embed(title="Removed User", description="User has been removed from the system", color=0x00ff00)
        embed.add_field(name="Removed User" + str(DiscordUser , inline=False))
      
        return embed

    def createListUsersEmbed(user_array):
        """
        creates a list of users embed for the listusers command
        """
        embed = discord.Embed(title="List of users", description="List of all users in the system", color=0x0000ff)
        for user in user_array:
            embed.add_field(name="User: " + user.get_name() + "("+user.Pronouns+")" , value="ID: " + str(user.UserID) + " is admin: " + str(user.ADMIN_PRIV), inline=False)
        return embed
        