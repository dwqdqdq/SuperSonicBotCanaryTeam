import discord
from discord.ext import commands
import os
import json
from glob import glob
import asyncio
from webserver import keep_alive
import random
from datetime import datetime


def read_token():
  with open("./assets/token.txt","r") as f:
    lines = f.readlines()
    return lines[0].strip()
  
token = read_token()

# with open(f"{os.getcwd()}/assets/config.json") as f:
#     config = json.load(f)

# token = config['token']
# prefix = config['prefix']

def get_prefix(client, message):
  with open('json/prefixes.json', 'r') as f:
    prefixes = json.load(f)
  try:
    return prefixes[str(message.guild.id)]
  except:
    return "PREFIX_ERROR"

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_message(message):
  if "PREFIX_ERROR":
    try:
      with open("json/prefixes.json", "r") as f:
        prefixes = json.load(f)
        prefixes[str(message.guild.id)] = "ssbc."
      with open("json/prefixes.json", "w") as f:
        json.dump(prefixes,f)
    except:
      return
  await client.process_commands(message)

@client.command(aliases=['pfp'])
async def stealpfp(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(f"Pfp Succesfully Ripped. lol {userAvatar}")

@client.command(aliases=['name'])
async def stealname(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userName = member.name
    await ctx.send(f"Name Succesfully Ripped. lol \n\nName: {userName}")
  
# for filename in os.listdir('./cogs'): #Calling out the cogs
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.{filename[:-3]}')

# for cog in os.listdir(r"cogs"):
#     if cog.endswith(".py"):
#         try:
#             cog = f"cogs.{cog.replace('.py', '')}"
#             client.load_extension(cog)
#         except Exception as e:
#             print(f"{cog} is failed to load:")
#             raise e

Cogs = [path.split("\\")[-1][:-3] for path in glob("./cogs/*.py")]

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")

page1 = discord.Embed(title="Help Page 1", description="This is the help page\n\nUse the buttons below to navigate between help pages.\n\n\n\nGENERAL COMMANDS\n\nssbc.help - Displays this message page.\n\nssbc.changeprefix - Changes the bot prefix.\n\nssbc.ping - Displays the bots latency.\n\nssbc.info - Displays info about the bot.\n\nssbc.links - Displays some helpful links.\n\nssbc.credits - Shows people involved in the development of this bot.\n\nssbc.poll - Creates a simple poll.\n\nssbc.reactrole - Creates a simple reaction role embed.\n(E.G: ssbc.reactrole ⬛  @rolename Text)\n\nssbc.say - Makes the bot say whatever you want.\n\nssbc.sayemb - Makes the bot say whatever you want in an embed.\n\nssbc.sayalt - Same as the other say command, but people can see who made a say message.\n\nssbc.sayembalt - Same as the other sayemb command, but people can see who made a sayemb message.", color=(16737304), timestamp=datetime.utcnow())

page2 = discord.Embed(title="Help Page 1a", description="CALCULATOR COMMANDS\n\nDon't ask lmao.\n\n(Command E.G: ssbc.mathadd 2 2)\n\nssbc.mathadd - Adds two numbers together.\n\nssbc.mathsub - Subtracts 2 numbers.\n\nssbc.mathrando - We don't exactly know what this command does. But maybe you do!\n\nssbc.mathdiv - Divides a number.\n\nssbc.mathmult - Multiplies a number.\n\nssbc.sqrt - A number that when multiplied by itself equals a given number.)", color=(16737304), timestamp=datetime.utcnow())

page3 = discord.Embed(title="Help Page 2", description="MODERATION COMMANDS\n\nssbc.clear - Clears a specified amount of messages.\n\nssbc.kick - Kicks a mentioned user.\n\nssbc.ban - Bans a mentioned user.\n\nssbc.unban - Unbans a specified user. (E.G: ssbc.unban User#0000)\n\nssbc.mute - Mutes a mentioned user.\n\nssbc.unmute - Unmutes a mentioned user.\n\nssbc.nuke - Nukes a channel (WARNING: This deletes ALL messages in a channel, use if you are completely sure you want to delete all messages in a channel.)\n\nssbc.snipe - Shows the last deleted message in a channel.", color=(16737304), timestamp=datetime.utcnow())

page4 = discord.Embed(title="Help Page 3", description="FUN COMMANDS\n\nssbc.8ball - Ask the magic 8ball questions! (Current Aliases: ssbc.chat)\n\nssbc.tictactoe - Play TicTacToe with another person\n(E.G: ssbc.tictactoe @player2)\nssbc.place - During TicTacToe, use 1-9 to place your marker on the board.\nssb.resign - Makes you resign from tictacto (Current Aliases: ssbc.forfiet)\n\nssb.c4 - Play Connect 4 with someone\n(E.G: ssbc.c4 @player2)", color=(16737304), timestamp=datetime.utcnow())

page5 = discord.Embed(title="Help Page 4", description="GIVEAWAY COMMANDS\n\nssbc.gstart - Starts a giveaway setup.\n\nssbc.gbasic - Starts a quick giveaway with only minutes. \n(example: gbasic 1 GiveawayName)\n\n(Please note you need a role named Giveaways to use these commands, even the owner", color=(16737304), timestamp=datetime.utcnow())

page6 = discord.Embed(title="Help Page 5", description="MUSIC COMMANDS\n\nssbc.connect - Makes the bot join your voice channel. \n(Current Aliases: ssbc.join)\n\nssbc.play - Makes the bot play a song from a youtube link or try and find the song by searching. (Current Aliases: ssbc.p)\n\nssbc.pause - Pauses a song currently playing.\n\nssbc.resume - Resumes a paused song.\n\nssbc.skip - Skips a song and plays a song next in the queue. \n(Current Aliases: ssbc.s)\n\nssbc.queue - Retrieve a basic queue of upcoming songs. \n(Current Aliases: ssbc.q, ssbc.playlist)\n\nssbc.volume - Changes the volume to a number between 1 and 100. (Current Aliases: ssbc.vol)\n\nssbc.stop - Stops a song and disconnects the bot. \n(Current Aliases: ssbc.leave, ssbc.disconnect, ssbc.l)\n\nssbc.reconnect - Makes the bot leave then join back \n(Current Aliases: ssbc.rejoin)\n\n\nSOUNDBOARD COMMANDS [WIP]\n\nssbc.tssintro - Makes the bot play TylerSuperSonic's intro song.\n\nssbc.tssoutro - Makes the bot play TylerSuperSonic's outro song.", color=(16737304), timestamp=datetime.utcnow())

client.help_pages = [page1, page2, page3, page4, page5, page6]

@client.command()
async def help(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=client.help_pages[current])
    embed = discord.Embed(title="**WARNING**", description="This bot is a Public Testing bot of the orignal SuperSonicBot. SuperSonicBot Canary may have commands that are either untested or unstable. If you feel unconfortable with untested commands, you can remove the bot.\n\n\nWant SuperSonicBot?\nDo ssbc.links", color=(11599872))
    await ctx.send(embed=embed)
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
          await msg.edit(content="Timed Out.")
          await msg.clear_reactions()

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if current < len(client.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(client.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=client.help_pages[current])

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(client.guilds)} Servers // ssbc.help'))
    print('Bot is ready.')
    for guild in client.guilds:
      print(f"Bot is in {guild.name}")


# @client.event
# async def on_message(ctx,messages):
#   if get_prefix() == "PREFIX_ERROR":
#     try:
#       ctx.send("Looks like theres a error with my prefix in this server! Attempting to fix it now.")
#       with open("json/prefixes.json", "r") as f:
#         prefixes = json.load(f)
#         prefixes[str(ctx.guild.id)] = "ssbc."
#         with open("json/prefixes.json", "w") as f:
#           json.dump(prefixes,f)
#     except:
#       ctx.send("Failed to reset prefix, please contact one of the developers.\nUse ssbc.credits to see the developers.")

#tictactoe

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p2: discord.Member):
     global count
     global player1
     global player2
     global turn
     global gameOver
     if p2.bot:
       await ctx.send("You can't play with a bot!") 
       return 

     if p2 == ctx.author:
       await ctx.send("You can't play with yourself!")
       return
     
     if gameOver:
         await ctx.send(f"{ctx.author.mention} has started a TicTacToe game!")

         global board
         board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                  ":white_large_square:", ":white_large_square:", ":white_large_square:",
                  ":white_large_square:", ":white_large_square:", ":white_large_square:"]
         turn = ""
         gameOver = False
         count = 0

         player1 = ctx.author
         player2 = p2

         # print the board
         line = ""
         for x in range(len(board)):
             if x == 2 or x == 5 or x == 8:
                 line += " " + board[x]
                 await ctx.send(line)
                 line = ""
             else:
                 line += " " + board[x]

         # determine who goes first
         num = random.randint(1, 2)
         if num == 1:
             turn = player1
             await ctx.send("It is <@" + str(player1.id) + ">'s turn.\n(Do ssbc.place [number] to mark a position.)")
         elif num == 2:
             turn = player2
             await ctx.send("It is <@" + str(player2.id) + ">'s turn.\n(Do ssbc.place [number] to mark a position.)")
     else:
         await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
     global turn
     global player1
     global player2
     global board
     global count
     global gameOver

     if not gameOver:
         mark = ""
         if turn == ctx.author:
             if turn == player1:
                 mark = ":regional_indicator_x:"
             elif turn == player2:
                 mark = ":o2:"
             if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
               board[pos - 1] = mark
               count += 1

               # print the board
               line = ""
               for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

               checkWinner(winningConditions, mark)
               print(count)
               if gameOver == True:
                      await ctx.send(mark + " wins!")
               elif count >= 9:
                 gameOver = True
                 await ctx.send("It's a tie!")

              # switch turns
               if turn == player1:
                    turn = player2
               elif turn == player2:
                    turn = player1
             else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
         else:
            await ctx.send("It is not your turn.")
     else:
        await ctx.send("Please start a new game using the tictactoe command.")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
      print(error)
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Please mention a player to play with.")
      elif isinstance(error, commands.BadArgument):
          await ctx.send(f"Please make sure to mention/ping a player (ie. {ctx.author.mention}).")

@place.error
async def place_error(ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Please enter a position you would like to mark.")
      elif isinstance(error, commands.BadArgument):
          await ctx.send("Please make sure to enter an integer.")

@client.command(aliases=['forfeit'])
async def resign(ctx):
    global gameOver
    global player1
    global player2
    if not gameOver:
        gameOver = True
        await ctx.send(f"{ctx.author.mention} has resigned!\nStart a new game using the tictactoe command.")
        return
    else:
      await ctx.send("There is currently no game running!")
      

keep_alive()
client.run(token)