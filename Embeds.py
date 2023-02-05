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
    

    def listConfiguration(personality_type, model_type, max_tokens, temperature, top_p, frequency_penalty, memory_length, responding_role, responding_channel, allow_non_whitelisted_users, user_array):
        """
        creates a list the configuration of the bot
        """
        embed = discord.Embed(title="List of configuration", description="List of all configuration in the system", color=0x0000ff)
        embed.add_field(name="Personality type" , value=personality_type, inline=False)
        embed.add_field(name="Model type" , value=model_type, inline=False)
        embed.add_field(name="Max tokens" , value=max_tokens, inline=False)
        embed.add_field(name="Temperature" , value=temperature, inline=False)
        embed.add_field(name="Top p" , value=top_p, inline=False)
        embed.add_field(name="Frequency penalty" , value=frequency_penalty, inline=False)
        embed.add_field(name="Memory length" , value=memory_length, inline=False)
        embed.add_field(name="Responding role" , value=responding_role, inline=False)
        embed.add_field(name="Responding channel" , value=responding_channel, inline=False)
        embed.add_field(name="Users" , value=user_array, inline=False)
        return embed
