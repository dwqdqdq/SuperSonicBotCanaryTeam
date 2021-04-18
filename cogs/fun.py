import discord
from discord.ext import commands
import random
import datetime
import asyncio
import praw
import giphy_client
from giphy_client.rest import ApiException
import json

reddit = praw.Reddit(client_id = "3x8bPejF3lTyPQ",
                     client_secret = "E7-k6V90lpIM5ZYX5ytrBWLjSc6LxQ",
                     username = "TylerSuperSonic_Py",
                     password = "pythonboi",
                     user_agent = "pythonpraw",
                     check_for_async=False)

def convert(time):
  pos = ["s","m","h","d"]

  time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

  unit = time[-1]

  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2


  return val * time_dict[unit]


class fun(commands.Cog):

  def __init__(self, commands):
      self.commands = commands

  @commands.Cog.listener()
  async def on_ready(self):
    print("Fun cog loaded")
  
  #reddit pic cmds

  @commands.command()
  async def meme(self,ctx):
    waitmsg = await ctx.send("Please wait...")
    
    subreddit = reddit.subreddit("memes")
    all_subs = []

    top = subreddit.top(limit = 100)

    for submission in top:
      all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name, color=(16737304))
    
    em.set_image(url = url)

    em.set_footer(text = f"Requested by {ctx.author.name}, Pictures from reddit.")

    await ctx.send(embed= em)

    await waitmsg.delete()
    
  @commands.command()
  async def cat(self,ctx):
    waitmsg = await ctx.send("Please wait...")
    
    subreddit = reddit.subreddit("cat")
    all_subs = []

    top = subreddit.top(limit = 100)

    for submission in top:
      all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name, color=(16737304))
    
    em.set_image(url = url)

    em.set_footer(text = f"Requested by {ctx.author.name}, Pictures from reddit.")

    await ctx.send(embed= em)

    await waitmsg.delete()

  @commands.command()
  async def dog(self,ctx):
    waitmsg = await ctx.send("Please wait...")

    subreddit = reddit.subreddit("dog")
    all_subs = []

    top = subreddit.top(limit = 100)

    for submission in top:
      all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name, color=(16737304))
    
    em.set_image(url = url)

    em.set_footer(text = f"Requested by {ctx.author.name}, Pictures from reddit.")

    await ctx.send(embed= em)

    await waitmsg.delete()
      
  @commands.command()
  async def snek(self,ctx):
    waitmsg = await ctx.send("Please wait...")

    subreddit = reddit.subreddit("snake")
    all_subs = []

    top = subreddit.top(limit = 100)

    for submission in top:
      all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name, color=(16737304))
    
    em.set_image(url = url)

    em.set_footer(text = f"Requested by {ctx.author.name}, Pictures from reddit.")


    await ctx.send(embed= em)

    await waitmsg.delete()

  #=============================================


  #giphy CMDs

  @commands.command()
  async def catgif(self,ctx,*,q="Cat"):
    waitmsg = await ctx.send("Please wait...")

    api_key="fjsgb0IMax8Tn6RQBd9xVj0o1bRXtYwv"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=100, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title="Okie dokie, Here is your random Cat gif. lol", color=(16737304))
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
        emb.set_footer(text = "Gifs from Giphy.")

        await ctx.channel.send(embed=emb)

        await waitmsg.delete()
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

  @commands.command()
  async def doggif(self,ctx,*,q="Dog"):

    api_key="fjsgb0IMax8Tn6RQBd9xVj0o1bRXtYwv"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=100, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title="Okie dokie, Here is your random Dog gif lol", color=(16737304))
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
        emb.set_footer(text = "Gifs from Giphy.")

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

  @commands.command()
  async def snekgif(self,ctx,*,q="Snake"):

    api_key="fjsgb0IMax8Tn6RQBd9xVj0o1bRXtYwv"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=100, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title="Okie dokie, Here is your random Snake gif lol", color=(16737304))
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
        emb.set_footer(text = "Gifs from Giphy.")

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

  #Other CMDs

  @commands.command(aliases=["chat", "8ball"])
  async def _8ball(self,ctx, *, question):
    responses = ["Yes",
                 "Maybe",
                 "Heck Yeah",
                 "No",
                 "My reply is no",
                 "Fuck no",
                 "¯\_(ツ)_/¯",
                 "Hi lol",
                 "I dont know that.",
                 "If you think I am answering that, you are mistaking me for another bot.",
                 "STOP BOTHERING ME!",
                 "How the fuck am I supposed to know that?!",
                 "IDFK LOL",
                 "No idea, leave me alone.",
                 "No... I mean yes... Well... Ask again later.",
                 "The answer is unclear... Seriously I double checked.",
                 "It's a coin flip really...",
                 "YesNoYesNoYesNoYesNoYesNo",
                 "Ask yourself this question in the mirror three times, the answer will become clear.",
                 "You want an answer? OK, here's your answer: ",
                 "No, fuck off.",
                 "Bruh no"]
    embed = discord.Embed(title="🎱8ball Question🎱", description=f"Question: {question}\nAnswer: {random.choice(responses)}\n\n\n(More answers possibly coming soon...)", color=(16737304))
    
    await ctx.send(embed = embed)


def setup(commands):
    commands.add_cog(fun(commands))