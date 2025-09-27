import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix = "!")

rankIndex = ["i1", "i2", "i3",
             "b1", "b2", "b3",
             "s1", "s2", "s3",
             "g1", "g2", "g3",
             "p1", "p2", "p3",
             "d1", "d2", "d3"]

rankList = ["Iron 1", "Iron 2", "Iron3",
            "Bronze 1", "Bronze 2", "Bronze 3",
            "Silver 1", "Silver 2", "Silver 3",
            "Gold 1", "Gold 2", "Gold 3",
            "Platinum 1", "Platinum 2", "Platinum 3",
            "Diamond 1", "Diamond 2", "Diamond 3"]

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_guild_join(guild):
    for i in rankList:
        if rankList.index(i) < 3:
            await guild.create_role(name=i, colour=discord.Colour.from_rgb(100, 100, 100), hoist=True)

        elif rankList.index(i) < 6:
            await guild.create_role(name=i, colour=discord.Colour.from_rgb(140, 90, 0), hoist=True)
            
        elif rankList.index(i) < 9:
            await guild.create_role(name=i, colour=discord.Colour.from_rgb(160, 160, 160), hoist=True)
            
        elif rankList.index(i) < 12:
            await guild.create_role(name=i, colour=discord.Colour.from_rgb(250, 170, 55), hoist=True)

        elif rankList.index(i) < 15:
            await guild.create_role(name=i, colour=discord.Colour.from_rgb(60, 165, 170), hoist=True)

        else:
            await guild.create_role(name=i, colour=discord.Colour.from_rgb(160, 110, 240), hoist=True)

@bot.command()
async def rank(context, arg):
    guild = context.guild
    member = context.author

    if arg in rankIndex:
        for i in member.roles:
            if i.name in rankList:
                await member.remove_roles(i)
                
        for i in guild.roles:
            if i.name == rankList[rankIndex.index(arg)]:
                newRank = guild.get_role(i.id)
                
        await member.add_roles(newRank)
        await context.send("Role updated")

    elif arg == "none":
        for i in member.roles:
            if i.name in rankList:
                await member.remove_roles(i)
                await context.send("Role updated")

    else:
        await context.send("Invalid command")
    
bot.run(TOKEN)

