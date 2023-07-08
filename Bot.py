import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', description="This is a Helper Bot", intents=intents)

BanList = [705541156850892841]


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="!commands"))
    print('Bot is online')


@bot.command()
async def msg(ctx, target1, message1):
    target2 = await bot.fetch_user(target1.replace("@", "").replace("<", "").replace(">", "").replace("!", ""))
    if ctx.author.id == BanList:
        await ctx.channel.send("⚠You are banned!⚠")
    else:
        await target2.send(str(message1) + " ~ from " + f'''<@{ctx.author.id}>''')
        print(str(message1) + " ~ de la " + f'''<@{ctx.author.id}>''')


@bot.command()
async def announce(ctx, message2):
    if ctx.author.id == BanList:
        await ctx.channel.send("⚠You are banned!⚠")
    elif ctx.author.guild_permissions.administrator:
        for member1 in ctx.guild.members:
            try:
                member2 = await bot.fetch_user(member1.id)
                await member2.send(str(message2) + " ~ announcement from " + f"""<@{ctx.author.id}>""")
                print(f"""-----announcement-----:{message2} by {ctx.author.id}""")
                break
            except:
                pass
    else:
        await ctx.channel.send("⚠You don't have permision to use this command!⚠")


@bot.command()
async def report(ctx, target3, reason):
    print(
        f"""-----!report!-----: {target3.replace("@", "").replace("<", "").replace(">", "").replace("!", "")} by {ctx.author.id} for {reason}""")


@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands", description="for @Bot DM#6773",
                          color=discord.Color.orange())
    embed.add_field(name="!msg", value="Send momone a message. example: !msg @DynoW#9056 You are the best!", inline=False)
    embed.add_field(name="!announce", value="(Admin only) Announce everyone on the server about something. example: !announce Ntza", inline=False)
    embed.add_field(name="!report", value="Send a report for an user. example: !report @BotDM scam", inline=False)
    embed.add_field(name="!website", value="Coming Soon!", inline=False)
    embed.set_footer(text="For help contact: DynoW#9056")
    await ctx.send(embed=embed)

load_dotenv()
bot.run(os.environ.get("DM_BOT_TOKEN"))
# https ://discordapp.com/oauth2/authorize?client_id=963110670155513876&scope=bot&permissions=0
