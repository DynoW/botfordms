import discord

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!comenzi | by Danutz'))
    print('Bot is ready.')


@client.event
async def on_message(message):
    if (message.content.startswith("!mesaj") or message.content.startswith("!msg")) and message.author != client.user:
        anunt = message.content.split()
        target = await client.fetch_user(
            anunt[1].replace("@", "").replace("<", "").replace(">", "").replace("!", ""))
        await target.send(str(anunt[2:]).replace("[", "").replace("]", "").replace("'", "").replace(",",
                                                                                                    "") + " ~ de la " + f'''<@{message.author.id}>''')
    if message.content.startswith("!comenzi") and message.author != client.user:
        embed = discord.Embed(title="Comenzi DM BOT", color=discord.Colour.red())
        embed.add_field(name="!mesaj", value="!mesaj (persoana) (textul) | Trimite cuiva un mesaj", inline=True)

        embed.set_footer(text="Pentru ajutor contactati: DynoW#9056")
        await message.channel.send(content=None, embed=embed)


client.run("OTYzMTEwNjcwMTU1NTEzODc2.YlRUtQ.Z0Asyu6aYL46DQNByR3cYaxwtnk")
# https ://discordapp.com/oauth2/authorize?client_id=963110670155513876&scope=bot&permissions=0
