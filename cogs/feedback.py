import discord
from discord.ext import commands
import json
from discord import DMChannel

master = [564941189539954708, 516264739500720157, 724723809218723970, 408076750644576266, 820693570423750677, 725935067569979442]

class Feedback(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("Feedback cog loaded")
  
  @commands.command()
  async def feedback(self, ctx, *, msg=''):
    embed = discord.Embed(title="Feedback Recieved!", description=f"**Feedback**: {msg}\n\n**Feedback By:** {ctx.author.mention}", color=(16737304))
    author = ctx.author
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    for x in master:
      try:
        user = await self.client.fetch_user(x)
        await DMChannel.send(user, embed=embed)
      except:
        pass
    await ctx.channel.send("**Feedback Sent Sucessfully**")


def setup(client):
  client.add_cog(Feedback(client))