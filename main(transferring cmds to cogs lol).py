import discord
from discord.ext import commands
import random
import datetime
import asyncio
from webserver import keep_alive
import os
from random import choice
import math
from dotenv import load_dotenv
import json
import praw #(reddit)
import giphy_client
from giphy_client.rest import ApiException


load_dotenv()

def get_prefix(client, message):
  with open('json/prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)
client.remove_command("help")

emb = discord.Embed(color=discord.Color.blue())

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('GTA 6 || ssbc.help'))
  print('Bot is ready.')

reddit = praw.Reddit(client_id = "3x8bPejF3lTyPQ",
                     client_secret = "E7-k6V90lpIM5ZYX5ytrBWLjSc6LxQ",
                     username = "TylerSuperSonic_Py",
                     password = "pythonboi",
                     user_agent = "pythonpraw",
                     check_for_async=False)

# def convert(time):
#   pos = ["s","m","h","d"]

#   time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

#   unit = time[-1]

#   if unit not in pos:
#     return -1
#   try:
#     val = int(time[:-1])
#   except:
#     return -2


#   return val * time_dict[unit]

def is_it_me(ctx):
    return ctx.author.id == 564941189539954708

@client.command()
@commands.check(is_it_me)
async def checkifowner(ctx):
    await ctx.send("Yes, you are the bot owner (This command is made for if someone claimed my bot is theirs.)")

# help pages
page1 = discord.Embed(title="Help Page 1", description="This is the help page\n\nUse the buttons below to navigate between help pages.\n\n\n\nGENERAL COMMANDS\n\nssbc.help - Displays this message page.\n\nssbc.ping - Displays the bots latency.\n\nssbc.changeprefix - Changes the bot prefix.\n\ntssbc.info - Displays info about the bot.\n\nssbc.links - Displays some helpful links.\n\nssbc.poll - Creates a simple poll.\n\nssbc.reactrole - Creates a simple reaction role embed.\n(E.G: ssbc.reactrole ⬛  @rolename Text)\n\nssbc.say - Makes the bot say whatever you want.\n\nssbc.sayemb - Makes the bot say whatever you want in an embed.\n\nssbc.sayalt - Same as the other say command, but people can see who made a say message.\n\nssbc.sayembalt - Same as the other sayemb command, but people can see who made a sayemb message.", color=(16737304))
page2 = discord.Embed(title="Help Page 1a", description="Don't ask lmao.\n\n\nCALCULATOR COMMANDS\n\n(Command E.G: ssbc.mathadd 2 2)\n\nssbc.mathadd - Adds two numbers together.\n\nssbc.mathsub - Subtracts 2 numbers.\n\nssbc.mathrando - We don't exactly know what this command does. But maybe you do!\n\nssbc.mathdiv - Divides a number.\n\nssbc.mathmult - Multiplies a number.\n\nssbc.sqrt - A number that when multiplied by itself equals a given number.)", color=(16737304))
page3 = discord.Embed(title="Help Page 2", description="MODERATION COMMANDS\n\nssbc.clear - Clears a specified amount of messages.\n\nssbc.kick - Kicks a mentioned user.\n\nssbc.ban - Bans a mentioned user.\n\nssbc.unban - Unbans a specified user. (E.G: ssbc.unban User#0000)\n\nssbc.mute - Mutes a mentioned user.\n\nssbc.unmute - Unmutes a mentioned user.\n\nssbc.nuke - Nukes a channel (WARNING: This deletes ALL messages in a channel, use if you are completely sure you want to delete all messages in a channel.)", color=(16737304))
page4 = discord.Embed(title="Help Page 3", description="FUN COMMANDS\n\nssbc.8ball - Ask the magic 8ball questions! (Current Aliases: ssbc.chat)\n\nssbc.tictactoe - Play TicTacToe with another person\n(E.G: ssbc.tictactoe @player2)\nssbc.place - During TicTacToe, use 1-9 to place your marker on the board.", color=(16737304))
page5 = discord.Embed(title="Help Page 4", description="GIVEAWAY COMMANDS\n\nssbc.gstart - Starts a giveaway setup.\n\nssbc.gbasic - Starts a quick giveaway with only minutes. \n(example: gbasic 1 GiveawayName)\n\n(Please note you need a role named Giveaways to use these commands, even the owner", color=(16737304))

client.help_pages = [page1, page2, page3, page4, page5]

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

@client.command()
async def helpold(ctx):
    embed = discord.Embed(title="**Help Page**", description="This is the help page\n\n\nGENERAL COMMANDS\n\nssbc.help - Displays this message page.\n\nssbc.ping - Displays the bots latency.\n\nssbc.info - Displays info about the bot.\n\nssbc.links - Displays some helpful links.\n\nssbc.poll - Creates a simple poll.\n\nssbc.say - Makes the bot say whatever you want.\n\nssbc.sayemb - Makes the bot say whatever you want in an embed.\n\nssbc.sayalt - Same as the other say command, but people can see who made a say message.\n\nssbc.sayembalt - Same as the other sayemb command, but people can see who made a sayemb message.\n\n\nMODERATION COMMANDS\n\nssbc.clear - Clears a specified amount of messages.\n\nssbc.kick - Kicks a mentioned user.\n\nssbc.ban - Bans a mentioned user.\n\nssbc.unban - Unbans a specified user. (E.G: ssbc.unban User#0000)\n\nssbc.mute - Mutes a mentioned user.\n\nssbc.unmute - Unmutes a mentioned user.\n\nssbc.nuke - Nukes a channel (WARNING: This deletes ALL messages in a channel, use if you are completely sure you want to delete all messages in a channel.)\n\n\nFUN COMMANDS\n\nssbc.8ball - Ask the magic 8ball questions! (Current Aliases: ssbc.chat)\n\n\nGIVEAWAY COMMANDS\n\nssbc.gstart - Starts a giveaway setup.\n\nssbc.gbasic - Starts a quick giveaway with only minutes. \n(example: gbasic 1 GiveawayName)\n\n(Please note you need a role named Giveaways to use these commands, even the owner)", color=(16737304))
    await ctx.send(embed=embed)
    
    embed = discord.Embed(title="**WARNING**", description="This bot is a Public Testing bot of the orignal SuperSonicBot. SuperSonicBot Canary may have commands that are either untested or unstable. If you feel unconfortable with untested commands, you can remove the bot.\n\n\nWant SuperSonicBot?\nDo ssbc.links", color=(11599872))
    await ctx.send(embed=embed)

@client.command()
async def links(ctx):
    embed = discord.Embed(title="**Helpful Links**", description="This is the links page\n\n------------------------\nInvite Bot: https://discord.com/oauth2/authorize?client_id=816034199244636201&permissions=8&scope=bot\n\n\nInvite Canary Bot: https://discord.com/oauth2/authorize?client_id=816114718351687690&permissions=8&scope=bot\n\n\nDiscord Support Server: https://discord.gg/byp2qEYpEw\n\n\nMy Website: https://tylersupersonicyt.wixsite.com/tssofficial/\n------------------------", color=(16737304))

    embed.set_footer(text = "Made by TylerSuperSonic")

    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(title="**Info Page**", description="This is the information page\n\n------------------------\nInvite Bot: SuperSonicBot Canary\n\nPrefix: ssbc.\n\nHosted using: https://repl.it/ and https://uptimerobot.com/\n\nMade using: Discord.py (Python)\n------------------------", color=(16737304))

    embed.set_footer(text = "Made by TylerSuperSonic")

    await ctx.send(embed=embed)

# @client.event
# async def on_raw_reaction_add(payload):

#     if payload.member.bot:
#         pass

#     else:
#         with open('reactrole.json') as react_file:
#             data = json.load(react_file)
#             for x in data:
#                 if x['emoji'] == payload.emoji.name:
#                     role = discord.utils.get(client.get_guild(
#                         payload.guild_id).roles, id=x['role_id'])

#                     await payload.member.add_roles(role)


# @client.event
# async def on_raw_reaction_remove(payload):

#     with open('reactrole.json') as react_file:
#         data = json.load(react_file)
#         for x in data:
#             if x['emoji'] == payload.emoji.name:
#                 role = discord.utils.get(client.get_guild(
#                     payload.guild_id).roles, id=x['role_id'])


#                 await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)


# @client.command()
# @commands.has_permissions(administrator=True, manage_roles=True)
# async def reactrole(ctx, emoji, role: discord.Role, *, message):

#     emb = discord.Embed(description=message)
#     msg = await ctx.channel.send(embed=emb)
#     await msg.add_reaction(emoji)

#     with open('reactrole.json') as json_file:
#         data = json.load(json_file)

#         new_react_role = {'role_name': role.name, 
#         'role_id': role.id,
#         'emoji': emoji,
#         'message_id': msg.id}

#         data.append(new_react_role)

#     with open('reactrole.json', 'w') as f:
#         json.dump(data, f, indent=4)

# @client.command()
# async def poll(ctx,*,message):
#     emb=discord.Embed(title="🤔Poll🤔", description=f"{message}", color=(16737304))
#     emb.add_field(name = "Poll By:", value = ctx.author.mention)
#     msg=await ctx.channel.send(embed=emb)
#     await msg.add_reaction('👍')
#     await msg.add_reaction('👎')

# @client.command()
# @commands.has_permissions(manage_messages=True)
# async def say(ctx, *, question):
#     await ctx.message.delete()
#     await ctx.send(f'{question}', allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False))

# @client.command()
# @commands.has_permissions(manage_messages=True)
# async def sayalt(ctx, *, question):
#     await ctx.message.delete()
#     await ctx.send(f'{question}\n\n**Said By:** {ctx.author.mention}', allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False))

# @client.command()
# @commands.has_permissions(manage_messages=True)
# async def sayemb(ctx,*,message):
#     await ctx.message.delete()
#     emb=discord.Embed(description=f"{message}", color=(16737304))
#     msg=await ctx.channel.send(embed=emb)

# @client.command()
# @commands.has_permissions(manage_messages=True)
# async def sayembalt(ctx,*,message):
#     await ctx.message.delete()
#     emb=discord.Embed(description=f"{message}", color=(16737304))
#     emb.add_field(name = "Said By:", value = ctx.author.mention)
#     msg=await ctx.channel.send(embed=emb)

# @say.error
# async def say_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send('**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help')
#     else:
#         raise error

# @sayalt.error
# async def sayalt_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send('**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help')
#     else:
#         raise error

# @sayemb.error
# async def sayemb_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send('**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help')
#     else:
#         raise error

# @sayembalt.error
# async def sayembalt_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send('**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help')
#     else:
#         raise error

# @client.command()
# @commands.has_role("Giveaways")
# async def gstart(ctx):
#     await ctx.send("The Giveaway is being set up, answer each of these questions within 15 seconds.")

#     questions = ["Which channel should the giveaway be hosted in?",
#                  "What should the duration of the giveaway be? (s,m,h,d)",
#                  "What is the Prize of the Giveaway?"]

#     answers = []

#     def check(m):
#         return m.author == ctx.author and m.channel == ctx.channel

#     for i in questions:
#         await ctx.send(i)

#         try:
#             msg = await client.wait_for('message', timeout=15.0, check=check)
#         except asyncio.TimeoutError:
#             await ctx.send("You didnt answer in time, try again later.")
#             return
#         else:
#             answers.append(msg.content)


#     try:
#         c_id = int(answers[0][2:-1])
#     except:
#         await ctx.send("You did not mention a channel correctly.")
#         return

#     channel = client.get_channel(c_id)

#     time = convert(answers[1])
#     if time == -1:
#         await ctx.send("You did not answer with the proper unit.")
#         return
#     elif time == -2:
#         await ctx.send("The time must be an integer.")
#         return

#     prize = answers[2]

#     await ctx.send(f"The Giveaway is setup and will now be hosted in {channel.mention}! It will last **{answers[1]}**, Good luck.")


#     embed = discord.Embed(title = "🎉🎉Giveaway!🎉🎉", description = f"**Prize:** {prize}", color = ctx.author.color)

#     embed.add_field(name = "Hosted By:", value = ctx.author.mention)
    
#     embed.set_footer(text = f"Ends {answers[1]} from now")

#     my_msg = await channel.send(embed = embed)


#     await my_msg.add_reaction("🎉")


#     await asyncio.sleep(time)


#     new_msg = await channel.fetch_message(my_msg.id)


#     users = await new_msg.reactions[0].users().flatten()
#     users.pop(users.index(client.user))

#     winner = random.choice(users)

#     await channel.send(f"Congratulations {winner.mention}! you won the **{prize}**!")

# @client.command()
# @commands.has_role("Giveaways")
# async def gbasic(ctx, mins : int, * , prize: str):
#     embed = discord.Embed(title = "🎉🎉Giveaway!🎉🎉", description = f"**Prize:** {prize}", color = ctx.author.color)
    

#     end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

#     embed.add_field(name = "Hosted By:", value = ctx.author.mention)
#     embed.add_field(name = "Ends At:", value = f"{end} UTC")
#     embed.set_footer(text = f"Ends {mins} minutes from now")

#     my_msg = await ctx.send(embed = embed)

#     await my_msg.add_reaction("🎉")


#     await asyncio.sleep(mins*60)


#     new_msg = await ctx.channel.fetch_message(my_msg.id)


#     users = await new_msg.reactions[0].users().flatten()
#     users.pop(users.index(client.user))

#     winner = random.choice(users)

#     await ctx.send(f"Congratulations {winner.mention}! You won the **{prize}**!")

# @client.command()
# @commands.has_role("Giveaways")
# async def gstartrig(ctx):
#     await ctx.send("The Giveaway is being set up, answer each of these questions within 15 seconds. ( ͡° ͜ʖ ͡°)")

#     questions = ["Which channel should the giveaway be hosted in?",
#                  "What should the duration of the giveaway be? (s,m,h,d)",
#                  "What is the Prize of the Giveaway?"]

#     answers = []

#     def check(m):
#         return m.author == ctx.author and m.channel == ctx.channel

#     for i in questions:
#         await ctx.send(i)

#         try:
#             msg = await client.wait_for('message', timeout=15.0, check=check)
#         except asyncio.TimeoutError:
#             await ctx.send("You didnt answer in time. Try again later.")
#             return
#         else:
#             answers.append(msg.content)


#     try:
#         c_id = int(answers[0][2:-1])
#     except:
#         await ctx.send("You did not mention a channel correctly.")
#         return

#     channel = client.get_channel(c_id)

#     time = convert(answers[1])
#     if time == -1:
#         await ctx.send("You did not answer with the proper unit.")
#         return
#     elif time == -2:
#         await ctx.send("The time must be an integer.")
#         return

#     prize = answers[2]

#     await ctx.send(f"The Giveaway is setup and will now be hosted in {channel.mention}! It will last **{answers[1]}**, Good luck.")


#     embed = discord.Embed(title = "🎉🎉Giveaway!🎉🎉", description = f"**Prize:** {prize}", color = ctx.author.color)

#     embed.add_field(name = "Hosted By:", value = ctx.author.mention)
    
#     embed.set_footer(text = f"Ends {answers[1]} from now")

#     my_msg = await channel.send(embed = embed)


#     await my_msg.add_reaction("🎉")


#     await asyncio.sleep(time)


#     new_msg = await channel.fetch_message(my_msg.id)


#     users = await new_msg.reactions[0].users().flatten()
#     users.pop(users.index(client.user))

#     winner = ctx.author

#     await channel.send(f"Congratulations {winner.mention}! you won the **{prize}**!")

# @client.command()
# async def ping(ctx):
#     await ctx.send(f'**PONG!**\n\nLatency: {round(client.latency * 1000)}ms')

# @client.command(aliases=["chat", "8ball"])
# async def _8ball(ctx, *, question):
#     responses = ["Yes",
#                  "Maybe",
#                  "Heck Yeah",
#                  "No",
#                  "My reply is no",
#                  "Fuck no",
#                  "¯\_(ツ)_/¯",
#                  "Hi lol",
#                  "I dont know that.",
#                  "If you think I am answering that, you are mistaking me for another bot.",
#                  "STOP BOTHERING ME!",
#                  "How the fuck am I supposed to know that?!",
#                  "IDFK LOL",
#                  "No idea, leave me alone.",
#                  "No... I mean yes... Well... Ask again later.",
#                  "The answer is unclear... Seriously I double checked.",
#                  "It's a coin flip really...",
#                  "YesNoYesNoYesNoYesNoYesNo",
#                  "Ask yourself this question in the mirror three times, the answer will become clear.",
#                  "You want an answer? OK, here's your answer: ",
#                  "No, fuck off."]
#     embed = discord.Embed(title="🎱8ball Question🎱", description=f"Question: {question}\nAnswer: {random.choice(responses)}\n\n\n(More answers possibly coming soon...)", color=(16737304))
    
#     await ctx.send(embed = embed)

# @client.command()
# async def meme(ctx):
#   subreddit = reddit.subreddit("memes")
#   all_subs = []

#   top = subreddit.top(limit = 50)

#   for submission in top:
#     all_subs.append(submission)

#   random_sub = random.choice(all_subs)

#   name = random_sub.title
#   url = random_sub.url

#   em = discord.Embed(title = name, color=(16737304))
  
#   em.set_image(url = url)

#   em.set_footer(text = "If it doesn't load, it was a video. Pictures from reddit.")

#   await ctx.send(embed= em)

# @client.command()
# async def catpic(ctx):
#   subreddit = reddit.subreddit("cat")
#   all_subs = []

#   top = subreddit.top(limit = 50)

#   for submission in top:
#     all_subs.append(submission)

#   random_sub = random.choice(all_subs)

#   name = random_sub.title
#   url = random_sub.url

#   em = discord.Embed(title = name, color=(16737304))
  
#   em.set_image(url = url)

#   em.set_footer(text = "If it doesn't load, it was a video. Pictures from reddit.")

#   await ctx.send(embed= em)

# @client.command()
# async def dogpic(ctx):
#   subreddit = reddit.subreddit("cat")
#   all_subs = []

#   top = subreddit.top(limit = 50)

#   for submission in top:
#     all_subs.append(submission)

#   random_sub = random.choice(all_subs)

#   name = random_sub.title
#   url = random_sub.url

#   em = discord.Embed(title = name, color=(16737304))
  
#   em.set_image(url = url)

#   em.set_footer(text = "If it doesn't load, it was a video. Pictures from reddit.")

#   await ctx.send(embed= em)

# @client.command()
# async def snekpic(ctx):
#   subreddit = reddit.subreddit("snake")
#   all_subs = []

#   top = subreddit.top(limit = 50)

#   for submission in top:
#     all_subs.append(submission)

#   random_sub = random.choice(all_subs)

#   name = random_sub.title
#   url = random_sub.url

#   em = discord.Embed(title = name, color=(16737304))
  
#   em.set_image(url = url)

#   em.set_footer(text = "If it doesn't load, it was a video. Pictures from reddit.")

#   await ctx.send(embed= em)

# @client.command(aliases=["cat"])
# async def _cat(ctx):
#     responses = ["https://cdn.discordapp.com/attachments/816144723277250580/819441406887329802/Cat2.jpg",
#                  "https://cdn.discordapp.com/attachments/816144723277250580/819441433849233418/Cat6.jpg",
#                  "https://cdn.discordapp.com/attachments/816144723277250580/819441459413516288/Cat5.jpg",
#                  "https://cdn.discordapp.com/attachments/816144723277250580/819441543302742036/Cat7.jpg",
#                  "https://cdn.discordapp.com/attachments/816144723277250580/819441589117911040/Cat1.jpg",
#                  "https://media.discordapp.net/attachments/816144723277250580/819451133910712350/unknown.gif",
#                  "https://media.discordapp.net/attachments/816144723277250580/819450592845758494/Cat3.jpg",
#                  "https://media.discordapp.net/attachments/816144723277250580/819450556887597086/Cat4s.jpg",
#                  "https://media.discordapp.net/attachments/816144723277250580/819450504451063828/Kitten2.jpg",
#                  "https://media.discordapp.net/attachments/816144723277250580/819450480534880256/Kitten9.jpg",
#                  "https://media.discordapp.net/attachments/816144723277250580/819451788218335282/meowthra.jpg",
#                  "https://tenor.com/view/no-nones-nop-gif-4708604"]
#     await ctx.send(f'Okie dokie, Here is you random Cat picture. lol\n\n {random.choice(responses)}')

# @client.command()
# async def catgif(ctx,*,q="Cat"):

#     api_key="fjsgb0IMax8Tn6RQBd9xVj0o1bRXtYwv"
#     api_instance = giphy_client.DefaultApi()

#     try: 
#     # Search Endpoint
        
#         api_response = api_instance.gifs_search_get(api_key, q, limit=100, rating='g')
#         lst = list(api_response.data)
#         giff = random.choice(lst)

#         emb = discord.Embed(title="Okie dokie, Here is you random Cat gif. lol", color=(16737304))
#         emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

#         await ctx.channel.send(embed=emb)
#     except ApiException as e:
#         print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

# @client.command()
# async def doggif(ctx,*,q="Dog"):

#     api_key="fjsgb0IMax8Tn6RQBd9xVj0o1bRXtYwv"
#     api_instance = giphy_client.DefaultApi()

#     try: 
#     # Search Endpoint
        
#         api_response = api_instance.gifs_search_get(api_key, q, limit=100, rating='g')
#         lst = list(api_response.data)
#         giff = random.choice(lst)

#         emb = discord.Embed(title="Okie dokie, Here is you random Dog gif lol", color=(16737304))
#         emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

#         await ctx.channel.send(embed=emb)
#     except ApiException as e:
#         print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

# player1 = ""
# player2 = ""
# turn = ""
# gameOver = True

# board = []

# winningConditions = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8],
#     [0, 3, 6],
#     [1, 4, 7],
#     [2, 5, 8],
#     [0, 4, 8],
#     [2, 4, 6]
# ]

# @client.command()
# async def tictactoe(ctx, p2: discord.Member):
#     global count
#     global player1
#     global player2
#     global turn
#     global gameOver
#     if p2.bot:
#       await ctx.send("You can't play with a bot!") 
#       return 
#     if gameOver:
#         global board
#         board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
#                  ":white_large_square:", ":white_large_square:", ":white_large_square:",
#                  ":white_large_square:", ":white_large_square:", ":white_large_square:"]
#         turn = ""
#         gameOver = False
#         count = 0

#         player1 = ctx.author
#         player2 = p2

#         # print the board
#         line = ""
#         for x in range(len(board)):
#             if x == 2 or x == 5 or x == 8:
#                 line += " " + board[x]
#                 await ctx.send(line)
#                 line = ""
#             else:
#                 line += " " + board[x]

#         # determine who goes first
#         num = random.randint(1, 2)
#         if num == 1:
#             turn = player1
#             await ctx.send("It is <@" + str(player1.id) + ">'s turn.\n(Do ssbc.place [number] to mark a position.)")
#         elif num == 2:
#             turn = player2
#             await ctx.send("It is <@" + str(player2.id) + ">'s turn.\n(Do ssbc.place [number] to mark a position.)")
#     else:
#         await ctx.send("A game is already in progress! Finish it before starting a new one.")

# @client.command()
# async def place(ctx, pos: int):
#     global turn
#     global player1
#     global player2
#     global board
#     global count
#     global gameOver

#     if not gameOver:
#         mark = ""
#         if turn == ctx.author:
#             if turn == player1:
#                 mark = ":regional_indicator_x:"
#             elif turn == player2:
#                 mark = ":o2:"
#             if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
#                 board[pos - 1] = mark
#                 count += 1

#                 # print the board
#                 line = ""
#                 for x in range(len(board)):
#                     if x == 2 or x == 5 or x == 8:
#                         line += " " + board[x]
#                         await ctx.send(line)
#                         line = ""
#                     else:
#                         line += " " + board[x]

#                 checkWinner(winningConditions, mark)
#                 print(count)
#                 if gameOver == True:
#                     await ctx.send(mark + " wins!")
#                 elif count >= 9:
#                     gameOver = True
#                     await ctx.send("It's a tie!")

#                 # switch turns
#                 if turn == player1:
#                     turn = player2
#                 elif turn == player2:
#                     turn = player1
#             else:
#                 await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
#         else:
#             await ctx.send("It is not your turn.")
#     else:
#         await ctx.send("Please start a new game using the !tictactoe command.")


# def checkWinner(winningConditions, mark):
#     global gameOver
#     for condition in winningConditions:
#         if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
#             gameOver = True

# @tictactoe.error
# async def tictactoe_error(ctx, error):
#     print(error)
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Please mention a player to play with.")
#     elif isinstance(error, commands.BadArgument):
#         await ctx.send("Please make sure to mention/ping a player (ie. <@688534433879556134>).")

# @place.error
# async def place_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Please enter a position you would like to mark.")
#     elif isinstance(error, commands.BadArgument):
#         await ctx.send("Please make sure to enter an integer.")

# #@client.command(pass_test=True)
# async def nuke(ctx, amount=10**10):
#   if not ctx.author.permissions_in(ctx.channel).manage_messages:
#     embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
#     await ctx.send(embed=embedm01)
#     return
#   await ctx.channel.purge(limit=amount)
#   await ctx.send('Channel successfully nuked at the speed of sound.\nhttps://imgur.com/LIyGeCR')
#   return


#@client.command()
# @commands.has_permissions(manage_messages=True)
# async def clear(ctx, amount=500):
#     if (amount > 501):
#       return await ctx.send("test to see if i didnt fuck up the code")
#     if (amount <= 0):
#         embedn01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE N01** \nNegative Value\n\nAre you stupid? you cant have negative numbers to clear messages. It should be something like this: ssbc.clear 10 <---- whole number\n\nSometimes I question your intellegence my friend", color=(16737304))
#         return await ctx.send(embed=embedn01)
#     await ctx.channel.purge(limit=amount)
#     msg = await ctx.send("Messages successfully deleted at the speed of sound, if they didn't this means there's an error.")
#     await asyncio.sleep(5)
#     await msg.delete()

#@clear.error
# async def clear_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
#         await ctx.send(embed=embedm01)
#     else:
#         raise error

#@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    if member == None or member == ctx.message.author:
        embeds01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE S01**\n\nYou cannot kick yourself stupid", color=(16737304))
        await ctx.channel.send(embed=embeds01)
        return
    if reason == None:
        reason = "For being dumb"
    await member.create_dm()
    embedofkickeddm = discord.Embed(title=f"{member.name}, You've been kicked from: \n`{ctx.guild.name}`", description=f'**Reason:** {reason}', color=(16737304))
    await member.dm_channel.send(embed=embedofkickeddm)
    await member.kick(reason=reason)
    embedofkicked = discord.Embed(title="🔧Kick Successful🔧", description=f'**Member Kicked:** <@!{member.id}>\n **Reason:** {reason}', color=(16737304))
    await ctx.send(embed=embedofkicked)

#@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command.\nYou need the ``kick members`` permission\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
    else:
        raise error
    
#@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    if member == None or member == ctx.message.author:
        embeds01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE S01**\n\nYou cannot ban yourself stupid", color=(16737304))
        await ctx.channel.send(embed=embeds01)
        return
    if reason == None:
        reason = "For being dumb"
    await member.create_dm()
    embedofbandm = discord.Embed(title=f"{member.name}, You've been banned from: \n`{ctx.guild.name}`", description=f'**Reason:** {reason}', color=(16737304))
    await member.dm_channel.send(embed=embedofbandm)
    await member.ban(reason=reason)
    embedofban = discord.Embed(title="🔨Ban Successful🔨", description=f'**Member Banned:** <@!{member.id}>\n **Reason:** {reason}', color=(16737304))
    await ctx.send(embed=embedofban)

#@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``ban members`` permission\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
    else:
        raise error

#@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
  banned_users = await ctx.guild.bans()
  member_name, member_disc = member.split('#')
  if member_name + member_disc == ctx.author.name + ctx.author.discriminator:
      embeds01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE S01**\n\nYou cannot unban yourself stupid and another fact is that YOU'RE NOT BANNED", color=(16737304))
      await ctx.send(embed=embeds01)
      return
  for ban_entry in banned_users:
    user = ban_entry.user
    if(user.name, user.discriminator)==(member_name,member_disc):
      await ctx.guild.unban(user)
      embedofunban = discord.Embed(title="🔨Unban Successful🔨", description=f'**Member Unbanned:** {member_name}',color=(16737304))
      await ctx.send(embed=embedofunban)
      return
    else:
      embedofnotfound = discord.Embed(title="**AN ERROR HAS OCCURRED - ERROR CODE N01**", description=f'**{member_name}#{member_disc}** was not found.',color=(16737304))
      await ctx.send(embed=embedofnotfound)
      return

#@client.command()
async def mute(ctx, member : discord.Member, *, reason=None):
  if (not ctx.author.guild_permissions.manage_messages):
    embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
    await ctx.send(embed=embedm01)
    return
  if(member.id == ctx.author.id):
    embeds01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE S01**\n\nYou cannot mute yourself stupid", color=(16737304))
    return await ctx.send(embed=embeds01)
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")

  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted")
    await ctx.send('No muted role found, Creating muted role...')
    
    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
  await member.add_roles(mutedRole, reason=reason)
  await ctx.send('Member successfully muted at the speed of sound.')

#@client.command()
async def unmute(ctx, member : discord.Member, *, reason=None):
  if (not ctx.author.guild_permissions.manage_messages):
    embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
    await ctx.send(embed=embedm01)
    return
  if(member.id == ctx.author.id):
    embeds01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE S01**\n\nYou cannot unmute yourself stupid", color=(16737304))
    return await ctx.send(embed=embeds01)
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")

  if not mutedRole:
    await ctx.send('**AN ERROR HAS OCCURRED - ERROR CODE S01**\n\nThis user is not muted.')
    return

  await member.remove_roles(mutedRole, reason=reason)
  await ctx.send('Member successfully unmuted at the speed of sound.')






# def add(n: float, n2: float):
# 	return n + n2

# def sub(n: float, n2: float):
# 	return n - n2

# def rando(n: int, n2: int):
# 	return random.randint(n, n2)

# def div(n: float, n2: float):
# 	return n / n2

# def sqrt(n: float):
# 	return math.sqrt(n)

# def mult(n: float, n2: float):
# 	return n * n2

# @client.command()
# async def mathadd(ctx, x: float, y: float):
# 	try:
# 		result = add(x, y)
# 		await ctx.send(f"**Number Added:** {result}")

# 	except:
# 		pass

# @client.command()
# async def mathsub(ctx, x: int, y: int):
# 	try:
# 		result = sub(x, y)
# 		await ctx.send(f"**Number Subtracted:** {result}")

# 	except:
# 		pass

# @client.command()
# async def mathrando(ctx, x: float, y: float):
# 	try:
# 		result = rando(x, y)
# 		await ctx.send(result)

# 	except:
# 		pass

# @client.command()
# async def mathdiv(ctx, x: float, y: float):
# 	try:
# 		result = div(x, y)
# 		await ctx.send(f"**Number Divided:** {result}")

# 	except:
# 		pass

# @client.command()
# async def mathmult(ctx, x: float, y: float):
# 	try:
# 		result = mult(x, y)
# 		await ctx.send(f"**Number Multiplied:** {result}")

# 	except:
# 		pass

# @client.command()
# async def mathsqrt(ctx, x: float):
# 	try:
# 		result = sqrt(x)
# 		await ctx.send(result)

# 	except:
# 		pass



@client.command()
async def credits(ctx):
    embed = discord.Embed(title="Credits", description="Head Developer: TylerSuperSonicYT#2251\nHelpers: MatthewTheHawk#6894, Risewill23#0023, s0nic26#4950, 》》• PokemonMaster •《《#7673\n\nSome commands were ripped from the following bots:\n\nBowser: https://discord.com/api/oauth2/authorize?client_id=799035921138974731&permissions=0&scope=bot", color=(16711680))
    await ctx.send(embed=embed)


# @client.event
# async def on_guild_join(guild):
#   with open('json/prefixes.json','r') as f:
#     prefixes = json.load(f)
          
#   prefixes[str(guild.id)] = "ssbc."

#   with open('json/prefixes.json', 'w') as f:
#     json.dump(prefixes, f, indent=4)

# @client.event
# async def on_guild_remove(guild):
#   with open('json/prefixes.json','r') as f:
#     prefixes = json.load(f)
  
#   prefixes.pop(str(guild.id))

#   with open('json/prefixes.json', 'w') as f:
#     json.dump(prefixes, f, indent=4)

# @client.command()
# async def changeprefix(ctx,prefix):
#   with open('json/prefixes.json', 'r') as f:
#     prefixes = json.load(f)
        
#   prefixes[str(ctx.guild.id)] = prefix

#   with open('json/prefixes.json', 'w') as f:
#     json.dump(prefixes, f, indent=4)

#   await ctx.send(f"Prefix successfully changed to ``{prefix}`` at the speed of sound.")

# @client.event
# async def on_message(message):
#   mention = f'<@!{client.user.id}>'
#   if message.guild:
#     with open("json/prefixes.json","r") as f:
#       prefixes = json.load(f)
#     pre = prefixes[str(message.guild.id)]
#     if pre in message.content:
#       pass
#     else:
#       if mention in message.content:
#         await message.channel.send(f"The prefix for this server is ``{pre}``")
#   await client.process_commands(message)

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)