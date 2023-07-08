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
    if ban_check(ctx.author.id) == True:
        await ctx.channel.send("⚠️ You are banned!⚠️")
    elif len(message1) == 0:
        await ctx.channel.send("Use: `!msg [user] [message]`")
    elif target1 == "all":
        if ctx.author.guild_permissions.administrator:
            for member1 in ctx.guild.members:
                try:
                    message = ' '.join(message1)
                    member2 = await bot.fetch_user(member1.id)
                    await member2.send(str(message) + " ~ announcement from " + f"""<@{ctx.author.id}>""")
                    print(f"""<-----announcement----->:{message} by {ctx.author.id}""")
                    break
                except:
                    pass
        else:
            await ctx.channel.send("⚠️ You don't have permision to use this command!⚠️")
    else:
        message = ' '.join(message1)
        target2 = await bot.fetch_user(target1.replace("@", "").replace("<", "").replace(">", "").replace("!", ""))
        await target2.send(str(message) + " ~ DM from " + f'''<@{ctx.author.id}>''')
        print(str(message) + " ~ de la " + f'''<@{ctx.author.id}>''')

@bot.command()
async def report(ctx, target3, *reason1):
    reason = ' '.join(reason1)
    print(
        f"""<-----!report!----->: {target3.replace("@", "").replace("<", "").replace(">", "").replace("!", "")} by {ctx.author.id} for {reason}""")
    await ctx.channel.send("Report sent!")

@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands for `@Bot DM#6773`", color=discord.Color.orange())
    embed.add_field(name="!msg", value="Send somone a message. example: `!msg @DynoW#9056 You are the best!`", inline=False)
    embed.add_field(name="!msg all", value="(Admin only) Announce everyone on the server about something. example: `!msg all Ntza`", inline=False)
    embed.add_field(name="!report", value="Send a report for an user. example: `!report @BotDM scam`", inline=False)
    embed.set_footer(text="For help contact: DynoW#9056")
    await ctx.send(embed=embed)

load_dotenv()
bot.run(os.environ.get("DM_BOT_TOKEN"))
# https ://discordapp.com/oauth2/authorize?client_id=963110670155513876&scope=bot&permissions=0
