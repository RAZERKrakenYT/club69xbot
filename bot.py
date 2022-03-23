import discord
from discord.utils import get
from discord.ext import commands
import shutil
import os
import asyncio
import random

client = commands.Bot(command_prefix = "=")

### Bot booting ###
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="on Twitch - ɾ Λ ʐ Ξ ɾ !!!", url="https://www.twitch.tv/razerezzzpzzzGG"))
    # await client.user.edit(username="CLOUDEX™")
    print("I am on service sir !")

### Member joining ###
@client.event
async def on_member_join(member: discord.Member):
    channel = await member.create_dm()
    await channel.send("Welcome to our CLOUDEX™ server!")
    
### Autorole ###    
@client.event
async def on_member_join(member): 
  role = discord.utils.get(member.guild.roles, name="BD")
  await member.add_roles(role)
    
### Member leaving ###
@client.event
async def on_member_remove(member: discord.Member):
    print(f"{member} has left this server!")
    channel = await member.create_dm()
    await channel.send("Sorry to see you go :frowning2:")

### Latency ###
@client.command()
async def ping(ctx):
    await ctx.send(f"Currently pinging at {round(client.latency*1000)}ms!")

### Deleting ###
@client.command()
@commands.has_role(".")
async def delete(ctx, amount=1):
    if amount==1:
        await ctx.send(f'{ctx.author.mention} Please define range of deletion after command.\nExample: "=delete 5"')
    else:
        await ctx.channel.purge(limit=amount+1)

### Kick ###
@client.command()
@commands.has_role(".")
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send(f"{member.mention} has been kicked!")

### Banning ###
@client.command()
@commands.has_role(".")
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send(f"{member.mention} has been banned!")

### Unbanning ###
@client.command()
@commands.has_role(".")
async def unban(ctx, *, member):
    banned_list = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    
    for ban_entry in banned_list:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} has been unbanned!")
            return

### Exception handling ###
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.author.mention} Oopppsss! Command not found!")

### Echoing ###
@client.command()
@commands.has_role(".")
async def echo(ctx):
    await ctx.channel.purge(limit=1)
    msg = ctx.message.content.split()
    output = ""
    for word in msg[1:]:
        output += word
        output += " "
    await ctx.channel.send(output)

### Dm a member ###
@client.command()
@commands.has_role(".")
async def dm(ctx, member: discord.Member, *, content):
    await ctx.channel.purge(limit=1)
    channel = await member.create_dm()
    await channel.send(content)
    await ctx.channel.send(f'"{content}" has been sent to {member}')

### User Avatar ###
@client.command()
async def avatar(ctx, member: discord.Member):
    embed=discord.Embed(color=0x229954)
    embed.set_author(name=member.name)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed= embed)
    #await ctx.send("{}".format(member.avatar_url))

### Random truth ###
@client.command()
async def truth(ctx, *, question):
    responses = ["That's fucking true!",
                 "You're God damn right!",
                 "No...That's not true!",
                 "That's impossible!",
                 "Maybe."]
    await ctx.send(f"{ctx.author.mention} {random.choice(responses)}")

### Random slang ###
@client.command()
async def slang(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    responses = ["Tui gay!",
                 "Biatch!",
                 "Piss off!",
                 "You are a Dick head!",
                 "Son of a gun!",
                 "You son of a gun!",
                 "You son of a motherless goat!",
                 ":DisappoinedMan:",
                 "You son of a mother trucker!",
                 "You Mothersmucker!",
                 "Poo on a stick!",
                 "Son of a biscuit!",
                 "Go lick a duck!",
                 "What the frog!",
                 "Yuck fou!",
                 "Tor hogay amar shona!",]
    await ctx.send(f"{member.mention} {random.choice(responses)}")
    
    ### Bot joining a voice channel ###
@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    
###### Music ######
@client.command()
@commands.has_role(".")
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')

### check if the bot is already playing ###
    else:
        await ctx.send("Bot is already playing")
        return


### command to resume voice if it is paused ###
@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')


### command to pause voice if it is playing ###
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')


### command to stop voice ###
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')


### Bot leaving a voice channel ###
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


client.run(os.environ['DISCORD_TOKEN'])
