import discord
from discord.ext import commands
from dotenv import load_dotenv
import json
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', description="This is a Helper Bot", intents=intents)

def ban_check(data):
    with open('BanList.json') as ban_file:
        list = json.load(ban_file)
        for banned in list["bans"]:
            print(banned)
            if banned["Id"] == data:
                return True
            else:
                return False


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="!commands"))
    print('Bot is online')


@bot.command()
async def msg(ctx, target1, *message1):
    if len(message1) == 0:
        await ctx.channel.send("Use: `!msg [user] [message]`")
    else:
        target2 = await bot.fetch_user(target1.replace("@", "").replace("<", "").replace(">", "").replace("!", ""))
        if ban_check(ctx.author.id) == True:
            await ctx.channel.send("⚠️ You are banned!⚠️")
        else:
            await target2.send(str(message1) + " ~ DM from " + f'''<@{ctx.author.id}>''')
            print(str(message1) + " ~ de la " + f'''<@{ctx.author.id}>''')


@bot.command()
async def ann(ctx, *message2):
    if len(message2) == 0:
        await ctx.channel.send("Use: `!ann [user] [message]`")
    else:
        if ban_check(ctx.author.id) == True:
            await ctx.channel.send("⚠️ You are banned!⚠️")
        elif ctx.author.guild_permissions.administrator:
            for member1 in ctx.guild.members:
                try:
                    member2 = await bot.fetch_user(member1.id)
                    await member2.send(str(message2) + " ~ announcement from " + f"""<@{ctx.author.id}>""")
                    print(f"""<-----announcement----->:{message2} by {ctx.author.id}""")
                    break
                except:
                    pass
        else:
            await ctx.channel.send("⚠️ You don't have permision to use this command!⚠️")


@bot.command()
async def report(ctx, target3, *reason):
    print(
        f"""<-----!report!----->: {target3.replace("@", "").replace("<", "").replace(">", "").replace("!", "")} by {ctx.author.id} for {reason}""")
    ctx.channel.send("Report sent!")

@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands", description="for @Bot DM#6773",
                          color=discord.Color.orange())
    embed.add_field(name="!msg", value="Send somone a message. example: !msg @DynoW#9056 You are the best!", inline=True)
    embed.add_field(name="!ann", value="(Admin only) Announce everyone on the server about something. example: !ann Ntza", inline=True)
    embed.add_field(name="!report", value="Send a report for an user. example: !report @BotDM scam", inline=True)
    embed.set_footer(text="For help contact: DynoW#9056")
    await ctx.send(embed=embed)

load_dotenv()
bot.run(os.environ.get("DM_BOT_TOKEN"))
# https ://discordapp.com/oauth2/authorize?client_id=963110670155513876&scope=bot&permissions=0
