import discord
from discord.ext import commands
from decouple import config


# Sets-up the discord bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(
    command_prefix="!", description="This is a Helper Bot", intents=intents
)


# Sets the bot presence
@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(name="!commands")
    )
    await bot.tree.sync()
    print("Bot is online")


# The command msg
@bot.tree.command(name='msg', description='Send a message to a user')
async def msg(interaction: discord.Interaction, user: discord.User, *, message: str):
    # # Ensure the user is not a bot
    # if user.bot:
    #     await interaction.response.send_message("You cannot send messages to bots.")
    #     return
    
    # The command for announcing something for all server
    if user.bot:
        # Checks if user of command has admin privileges on the server
        if interaction.user.guild_permissions.administrator:
            # Loops for member in server
            m_count=0
            u_count=""
            for member in interaction.guild.members:
                # Tries to send a message
                try:
                    await member.send(message+ " ~ announcement from "
                        + f"""<@{interaction.user.id}>""")
                    m_count+=1
                    u_count=u_count+member.name+" "
                except:
                    pass
            await interaction.response.send_message(f"Sent announcement to {str(m_count)} users.")
            print(f"""<-----announcement----->:"{message}" by {interaction.user.id}""")
            print("Users: " + u_count + "\n" + "User count: " + str(m_count))
        else:
            await interaction.response.send_message(
                "⚠️ You don't have permision to use this command! ⚠️"
            )
    else:
        # The command for sending a DM
        try:
            await user.send(message + " ~ DM from " + f"""<@{interaction.user.id}>""")
            print(str(message) + " ~ from " + f"""{interaction.user}({interaction.user.id})""" + " to " + f"""{user}({user.id})""")
            await interaction.response.send_message(f"Message sent to <@{user.id}>: {message}")
        except discord.errors.HTTPException:
            await interaction.response.send_message("Failed to send the message. Please check the user's privacy settings.")
            


# The commands of the bot
@bot.tree.command(name='help', description='Show commands for Bot DM')
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Commands for **@Bot DM#6773**", color=discord.Color.orange()
    )
    embed.add_field(
        name="**/msg [user] [message]**",
        value="> Send someone a message.\n> example: `!msg @DynoW#9056 You are the best!`",
        inline=False,
    )
    embed.add_field(
        name="**/msg @Bot DM [message]**",
        value="> (Admin only) Announce everyone on the server about something.\n> example: `!msg all Ntza`",
        inline=False,
    )
    embed.set_footer(text="For help contact: DynoW#9056")
    await interaction.response.send_message(embed=embed)


bot.run(config("DM_BOT_TOKEN"))
