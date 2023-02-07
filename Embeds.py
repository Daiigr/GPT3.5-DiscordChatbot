import discord
import datetime
class UserManagementEmbeds:
    def createAddedUserEmbed(DiscordUser, name, pronouns):
        embed = discord.Embed(title="Added User: " + name , color=0x90EE90)
        embed.set_author(name=DiscordUser.name, icon_url=DiscordUser.display_avatar)
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="User Configuration for " + str(DiscordUser), value="as " + name + "("+pronouns+")" , inline=False)
        return embed
    
    def createRemovedUserEmbed(DiscordUser):
        embed = discord.Embed(title="Removed User: " + str(DiscordUser) , color=0xFFCCCB)
        embed.set_author(name=DiscordUser.name, icon_url=DiscordUser.display_avatar)
        embed.timestamp = datetime.datetime.utcnow()
        return embed

    def createListUsersEmbed( user_array):
        """
        creates a list of users embed for the listusers command
        """
        embed = discord.Embed(title="List of Registered Users", description="List of all users in the system", color=0xFDEE73)
        for user in user_array:
            embed.add_field(name=f"{user.get_name()} ({user.Pronouns})", value=f" Admin: {'Yes' if user.ADMIN_PRIV else 'No'}", inline=False)
            embed.timestamp = datetime.datetime.utcnow()
        return embed

    
    def createListConfigurationEmbed(DEFAULT_PERSONALITY_TYPE, MODEL_TYPE, MAX_TOKENS, TEMPERATURE, TOP_P, FREQUENCY_PENALTY, PRESENCE_PENALTY):
        """
        creates a list the configuration of the bot
        """
        embed = discord.Embed(title="List of Configuration", description="List of all configurations in the system", color=0x800080)
        embed.add_field(name="Personality Type", value=DEFAULT_PERSONALITY_TYPE, inline=False)
        embed.add_field(name="Model Type", value=MODEL_TYPE, inline=False)
        embed.add_field(name="Max Tokens", value=MAX_TOKENS, inline=False)
        embed.add_field(name="Temperature", value=TEMPERATURE, inline=False)
        embed.add_field(name="Top P", value=TOP_P, inline=False)
        embed.add_field(name="Frequency Penalty", value=FREQUENCY_PENALTY, inline=False)
        embed.add_field(name="Presence Penalty", value=PRESENCE_PENALTY, inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        return embed
