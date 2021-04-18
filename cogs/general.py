#Libraries
import discord
from discord.ext import commands 
import json
import os
import asyncio
import traceback
import sys

def get_prefix(client, message):
  with open('json/prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix,intents=discord.Intents.all())

# Dev list ids
devslist = [724723809218723970,820693570423750677,516264739500720157,576857928913649684,408076750644576266,725935067569979442,564941189539954708]
#================================

class general(commands.Cog):

  def __init__(self, client):
      self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("General cog loaded")

  @commands.command()
  async def ping(self, ctx):
      embed = discord.Embed(title= 'Pong!', description= f'**{round(self.client.latency * 1000)}ms** :ping_pong:', color=(16737304) )
      await ctx.send(embed=embed)

  @commands.command()
  async def info(self,ctx):
    embed = discord.Embed(title="**Info Page**", description="This is the information page\n\n------------------------\nMade By: <@564941189539954708>\n\nName: SuperSonicBot Canary\n\nPrefix: ssbc.\n\nHosted using: https://repl.it/ and https://uptimerobot.com/\n\nMade using: Discord.py (Python)\n------------------------", color=(16737304))

    embed.set_footer(text = "Made by TylerSuperSonic")

    await ctx.send(embed=embed)

  @commands.command()
  async def links(self,ctx):
    embed = discord.Embed(title="**Helpful Links**", description="This is the links page\n\n------------------------\nInvite Bot: https://discord.com/api/oauth2/authorize?client_id=822992832343834656&permissions=8&scope=bot\n\n\nInvite Canary Bot: https://discord.com/api/oauth2/authorize?client_id=822996071508475904&permissions=8&scope=bot\n\n\nDiscord Support Server: https://discord.gg/byp2qEYpEw\n\n\nMy Website: https://tylersupersonicyt.wixsite.com/tssofficial/\n------------------------", color=(16737304))

    embed.set_footer(text = "Made by TylerSuperSonic")

    await ctx.send(embed=embed)

  @commands.command()
  async def credits(self,ctx):
    embed = discord.Embed(title="Credits", description="Head Developer: <@564941189539954708>\n\nHelpers: <@724723809218723970>, <@516264739500720157>, <@408076750644576266>,\n <@725935067569979442>, <@820693570423750677>\n<@576857928913649684>\n\nSome commands were ripped from the following bots:\n\nBowser: https://discord.com/api/oauth2/authorize?client_id=799035921138974731&permissions=0&scope=bot", color=(16711680))
    await ctx.send(embed=embed)

  @commands.command()
  async def poll(self,ctx,*,message):
    emb=discord.Embed(title="🤔Poll🤔", description=f"{message}", color=(16737304))
    emb.add_field(name = "Poll By:", value = ctx.author.mention)
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
  
  #say cmds

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def say(self,ctx, *, question):
    await ctx.message.delete()
    await ctx.send(f'{question}', allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False))
    
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def sayalt(self,ctx, *, question):
    await ctx.message.delete()
    await ctx.send(f'{question}\n\n**Said By:** {ctx.author.mention}', allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False))
    
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def sayemb(self,ctx,*,message):
    await ctx.message.delete()
    emb=discord.Embed(description=f"{message}", color=(16737304))
    msg=await ctx.channel.send(embed=emb)
    
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def sayembalt(self,ctx,*,message):
    await ctx.message.delete()
    emb=discord.Embed(description=f"{message}", color=(16737304))
    emb.add_field(name = "Said By:", value = ctx.author.mention)
    msg=await ctx.channel.send(embed=emb)

  #say errors

  @say.error
  async def say_error(self,ctx, error):
     if isinstance(error, commands.MissingPermissions):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
     else:
         raise error

  @sayalt.error
  async def sayalt_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
            await ctx.send(embed=embedm01)
        else:
            raise error

  @sayemb.error
  async def sayemb_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
            await ctx.send(embed=embedm01)
        else:
            raise error

  @sayembalt.error
  async def sayembalt_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
            await ctx.send(embed=embedm01)
        else:
            raise error

  #LOAD CMDS

  @commands.command()
  async def reloadcog(self, ctx, cog=None):
        checkdev = False
        for x in devslist:
          if(ctx.author.id == x):
            checkdev = True
            break
        if(checkdev == False):
          embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nYou don't own this bot\n\nSorry, you are not allowed to use this command. Only the bot devs is allowed to use this command.", color=(16737304))
          await ctx.send(embed=embedm01)
          return
        
        if not cog:
            # No cog, means we reload all cogs
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.client.unload_extension(f"cogs.{ext[:-3]}")
                            self.client.load_extension(f"cogs.{ext[:-3]}")
                            embed.add_field(
                                name=f"Reloaded: `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: `{ext}`",
                                value=e,
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)
        else:
            # reload the specific cog
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`",
                        value="This cog does not exist.",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.client.unload_extension(f"cogs.{ext[:-3]}")
                        self.client.load_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"Failed to reload: `{ext}`",
                            value=desired_trace,
                            inline=False
                        )
                await ctx.send(embed=embed)

  def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
  @commands.command()
  async def restart(self, ctx):
    checkdev = False
    for x in devslist:
      if(ctx.author.id == x):
        checkdev = True
        break
    if(checkdev == False):
      embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nYou don't own this bot\n\nSorry, you are not allowed to use this command. Only the bot devs is allowed to use this command.", color=(16737304))
      await ctx.send(embed=embedm01)
      return
          
    embed=discord.Embed(color=(16737304))
    embed.add_field(name=f"{self.client.user.name}Bot", value="Restarting", inline=False)
    await ctx.send(embed=embed)

    restart_program()
    
  
  @commands.command()
  async def shutdown(self, ctx):
    checkdev = False
    for x in devslist:
      if(ctx.author.id == x):
        checkdev = True
        break
    if(checkdev == False):
      embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nYou don't own this bot\n\nSorry, you are not allowed to use this command. Only the bot devs is allowed to use this command.", color=(16737304))
      await ctx.send(embed=embedm01)
      return

    embed=discord.Embed(color=(16737304))
    embed.add_field(name=f"{self.client.user.name} Bot", value="Shutting down, please allow up to 2 minutes for the bot to appear offline.", inline=False)
    await ctx.send(embed=embed)

    await ctx.bot.logout()
    


def setup(client):
    client.add_cog(general(client))