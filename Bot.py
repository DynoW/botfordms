import discord
from discord.ext import commands
import json
from decouple import config


# Set-up discord bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(
    command_prefix="!", description="This is a Helper Bot", intents=intents
)


# Function for checking if an user is banned from using a bot
# (for unban just delete the entry in BanList.json)
def ban_check(data):
    with open("BanList.json", "r") as ban_file:
        list = json.load(ban_file)
        for banned in list["bans"]:
            if banned["Id"] == data:
                return True
            else:
                return False


# Function for replacing symbols in user id
def get_uid(data):
    uid = data.replace("@", "").replace("<", "").replace(">", "").replace("!", "")
    return uid


# Set the bot presence
@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(name="!commands")
    )
    print("Bot is online")


# The command msg
@bot.command()
async def msg(ctx, target1=None, *message1):
    # Check if user is banned with the function ban_check()
    if ban_check(str(ctx.author.id)) == True:
        await ctx.channel.send("⚠️ You are banned! ⚠️")

    # Check if target is empty
    elif target1 == None:
        await ctx.channel.send("Use: `!msg [@user] [message]`")

    # Check if message is empty
    elif len(message1) == 0:
        await ctx.channel.send("Use: `!msg [@user] [message]`")

    # The command for announcing something for all server
    elif target1 == "all":
        # Checks if user of command has admin privileges on the server
        if ctx.author.guild_permissions.administrator:
            # Loops for member in server
            for member1 in ctx.guild.members:
                # Tries to send a message
                try:
                    message = " ".join(message1)
                    member2 = await bot.fetch_user(member1.id)
                    await member2.send(
                        str(message)
                        + " ~ announcement from "
                        + f"""<@{ctx.author.id}>"""
                    )
                    print(f"""<-----announcement----->:{message} by {ctx.author.id}""")
                    break
                except:
                    pass
        else:
            await ctx.channel.send(
                "⚠️ You don't have permision to use this command! ⚠️"
            )

    # The command for banning someone
    elif target1 == "block" or target1 == "ban":
        # Checks if user of command has admin privileges on the server
        if ctx.author.guild_permissions.administrator:
            # Adds the user id to BanList.json
            message2 = message1[0]
            with open("BanList.json", "r") as ban_file:
                list = json.load(ban_file)
            list["bans"] = list["bans"] + [{"Id": message2}]
            with open("BanList.json", "w") as ban_file:
                json.dump(list, ban_file)
        else:
            await ctx.channel.send(
                "⚠️ You don't have permision to use this command! ⚠️"
            )
    else:
        # The command for sending a DM
        try:
            message = " ".join(message1)
            target2 = await bot.fetch_user(get_uid(target1))
            await target2.send(str(message) + " ~ DM from " + f"""<@{ctx.author.id}>""")
            print(str(message) + " ~ de la " + f"""<@{ctx.author.id}>""")
        except:
            await ctx.channel.send("⚠️ ERROR! ⚠️ Can't send message to user!")


# The report command
@bot.command()
async def report(ctx, target3=None, *reason1):
    # Check the arguments
    if target3 == None:
        await ctx.channel.send("Use: `!report [@user] [message]`")
    elif len(reason1) == 0:
        await ctx.channel.send("Use: `!report [@user] [message]`")
    else:
        # Send report
        reason = " ".join(reason1)
        print(
            f"""<-----!report!----->: {get_uid(target3)} by {ctx.author.id} for: {reason}"""
        )
        await ctx.channel.send("Report sent!")


# The commands of the bot
@bot.command()
async def commands(ctx):
    embed = discord.Embed(
        title="Commands for **@Bot DM#6773**", color=discord.Color.orange()
    )
    embed.add_field(
        name="**!msg [user] [message]**",
        value="> Send someone a message.\nexample: `!msg @DynoW#9056 You are the best!`",
        inline=False,
    )
    embed.add_field(
        name="**!msg all [message]**",
        value="> (Admin only) Announce everyone on the server about something.\nexample: `!msg all Ntza`",
        inline=False,
    )
    embed.add_field(
        name="**!msg block [message]**",
        value="> (Admin only) Block a user.\nexample: `!msg block @BotDM`",
        inline=False,
    )
    embed.add_field(
        name="**!report [user] [message]**",
        value="> Send a report for an user.\nexample: `!report @BotDM scam`",
        inline=False,
    )
    embed.set_footer(text="For help contact: DynoW#9056")
    await ctx.send(embed=embed)


bot.run(config("DM_BOT_TOKEN"))
