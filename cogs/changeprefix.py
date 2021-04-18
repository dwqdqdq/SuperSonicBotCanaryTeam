import discord
from discord.ext import commands
import json

def get_prefix(client,message):
  with open("json/prefixes.json", "r") as f:
      prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

class ChangePrefix(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("ChangePrefix cog loaded")
  
  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    with open("json/prefixes.json", "r") as f:
      prefixes = json.load(f)

    prefixes[str(guild.id)] = "ssbc."

    with open("json/prefixes.json", "w") as f:
        json.dump(prefixes,f)

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def changeprefix(self,ctx,prefix):
    with open("json/prefixes.json", "r") as f:
      prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("json/prefixes.json", "w") as f:
      json.dump(prefixes,f)    

    await ctx.send(f"My prefix for this server was changed to ``{prefix}``")
  
  @commands.Cog.listener()
  async def on_message(self, msg):
    try:
      if msg.mentions[0] == self.client.user:
        with open("json/prefixes.json", "r") as f:
          prefixes = json.load(f)

        pre = prefixes[str(msg.guild.id)] 

        await msg.channel.send(f"My prefix for this server is ``{pre}``")

    except:
        pass

def setup(client):
  client.add_cog(ChangePrefix(client))





  
