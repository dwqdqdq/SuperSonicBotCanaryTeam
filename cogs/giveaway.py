import discord
from discord.ext import commands
import random
import datetime
import asyncio
from random import choice

def convert(time):
  pos = ["s","m","h","d"]

  time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

  unit = time[-1]

  if unit not in pos:
    return "ERR1"
  try:
    val = int(time[:-1])
  except:
    return "ERR2"


  return val * time_dict[unit]


class Giveaway(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Giveaway cog loaded")


  #advanced giveaway command

  @commands.command()
  @commands.has_role("Giveaways")
  async def gstart(self,ctx):
      await ctx.send("The Giveaway is being set up, answer each of these questions within 30 seconds.")

      questions = ["Which channel should the giveaway be hosted in?",
                  "What should the duration of the giveaway be? (s,m,h,d)",
                  "What is the Prize of the Giveaway?"]

      answers = []

      def check(m):
          return m.author == ctx.author and m.channel == ctx.channel

      for i in questions:
          await ctx.send(i)

          try:
              msg = await self.client.wait_for('message', timeout=30.0, check=check)
          except asyncio.TimeoutError:
              await ctx.send("You didnt answer in time, try again later.")
              return
          else:
              answers.append(msg.content)


      try:
          c_id = int(answers[0][2:-1])
      except:
          await ctx.send("You did not mention a channel correctly.")
          return

      channel = self.client.get_channel(c_id)

      time = convert(answers[1])
      if time == "ERR1":
          await ctx.send("You did not answer with the proper unit.")
          return
      elif time == "ERR2":
          await ctx.send("The time must be an integer.")
          return
      elif time < 0: 
          await ctx.send("The time has to be greater than 0.")
          return
      prize = answers[2]

      await ctx.send(f"The Giveaway is setup and will now be hosted in {channel.mention}! It will last **{answers[1]}**, Good luck.")


      msg = embed = discord.Embed(title = "🎉🎉**GIVEAWAY STARTING**🎉🎉", description = f"**Prize:** {prize}", color = ctx.author.color)

      embed.add_field(name = "Hosted By:", value = ctx.author.mention)
      
      ended = embed.set_footer(text = f"Ends {answers[1]} from now")

      my_msg = await channel.send(embed = embed)


      await my_msg.add_reaction("🎉")


      await asyncio.sleep(time)


      new_msg = await channel.fetch_message(my_msg.id)


      users = await new_msg.reactions[0].users().flatten()
      users.pop(users.index(self.client.user))

      winner = random.choice(users)

      ended = discord.Embed(title = "🎉🎉**GIVEAWAY ENDED**🎉🎉", description = f"**Winner:** {winner.mention}", color = ctx.author.color)

      ended.add_field(name = "Hosted By:", value = ctx.author.mention)
      
      ended.set_footer(text = "Ended")

      await my_msg.edit(embed=ended)

      await channel.send(f"Congratulations {winner.mention}! you won the **{prize}**!")

      if winner == None:
        ctx.send("Test")



  @gstart.error
  async def gstart_error(self,ctx, error):
      if isinstance(error, commands.MissingRole):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Roles\n\nSorry, you are not allowed to use this command. You need a role named ``Giveaways`` to create a giveaway.\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
      else:
        raise error







  #basic giveaway command


  @commands.command()
  @commands.has_role("Giveaways")
  async def gbasic(self,ctx, mins : int, * , prize: str):
      embed = discord.Embed(title = "🎉🎉Giveaway!🎉🎉", description = f"**Prize:** {prize}", color = ctx.author.color)
      

      end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

      embed.add_field(name = "Hosted By:", value = ctx.author.mention)
      embed.add_field(name = "Ends At:", value = f"{end} UTC")
      embed.set_footer(text = f"Ends {mins} minutes from now")

      my_msg = await ctx.send(embed = embed)

      await my_msg.add_reaction("🎉")


      await asyncio.sleep(mins*60)


      new_msg = await ctx.channel.fetch_message(my_msg.id)


      users = await new_msg.reactions[0].users().flatten()
      users.pop(users.index(self.client.user))

      winner = random.choice(users)

      ended = discord.Embed(title = "🎉🎉**GIVEAWAY ENDED**🎉🎉", description = f"**Winner:** {winner.mention}", color = ctx.author.color)

      ended.add_field(name = "Hosted By:", value = ctx.author.mention)
      
      ended.set_footer(text = "Ended")

      await my_msg.edit(embed=ended)

      await ctx.send(f"Congratulations {winner.mention}! You won the **{prize}**!")

  @gbasic.error
  async def gbasic_error(self,ctx, error):
      if isinstance(error, commands.MissingRole):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Roles\n\nSorry, you are not allowed to use this command. You need a role named ``Giveaways`` to create a giveaway.\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
      else:
        raise error











  #rigged giveaway
  @commands.command()
  @commands.has_role("Giveaways")
  async def gstartrig(self,ctx):
      await ctx.send("The Giveaway is being set up, answer each of these questions within 30 seconds. ( ͡° ͜ʖ ͡°)")

      questions = ["Which channel should the giveaway be hosted in?",
                  "What should the duration of the giveaway be? (s,m,h,d)",
                  "What is the Prize of the Giveaway?"]

      answers = []

      def check(m):
          return m.author == ctx.author and m.channel == ctx.channel

      for i in questions:
          await ctx.send(i)

          try:
              msg = await self.client.wait_for('message', timeout=30.0, check=check)
          except asyncio.TimeoutError:
              await ctx.send("You didnt answer in time, try again later.")
              return
          else:
              answers.append(msg.content)


      try:
          c_id = int(answers[0][2:-1])
      except:
          await ctx.send("You did not mention a channel correctly.")
          return

      channel = self.client.get_channel(c_id)

      time = convert(answers[1])
      if time == "ERR1":
          await ctx.send("You did not answer with the proper unit.")
          return
      elif time == "ERR2":
          await ctx.send("The time must be an integer.")
          return
      elif time < 0: 
          await ctx.send("The time has to be greater than 0.")
          return
      prize = answers[2]

      await ctx.send(f"The Giveaway is setup and will now be hosted in {channel.mention}! It will last **{answers[1]}**, Good luck.")


      msg = embed = discord.Embed(title = "🎉🎉**GIVEAWAY STARTING**🎉🎉", description = f"**Prize:** {prize}", color = ctx.author.color)

      embed.add_field(name = "Hosted By:", value = ctx.author.mention)
      
      ended = embed.set_footer(text = f"Ends {answers[1]} from now")

      my_msg = await channel.send(embed = embed)


      await my_msg.add_reaction("🎉")


      await asyncio.sleep(time)


      new_msg = await channel.fetch_message(my_msg.id)


      users = await new_msg.reactions[0].users().flatten()
      users.pop(users.index(self.client.user))

      winner = ctx.author

      ended = discord.Embed(title = "🎉🎉**GIVEAWAY ENDED**🎉🎉", description = f"**Winner:** {winner.mention}", color = ctx.author.color)

      ended.add_field(name = "Hosted By:", value = ctx.author.mention)
      
      ended.set_footer(text = "Ended")

      await my_msg.edit(embed=ended)

      await channel.send(f"Congratulations {winner.mention}! you won the **{prize}**!")

  @gstartrig.error
  async def gstartrig_error(self,ctx, error):
      if isinstance(error, commands.MissingRole):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Roles\n\nSorry, you are not allowed to use this command. You need a role named ``Giveaways`` to create a giveaway.\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
      else:
        raise error

def setup(client):
  client.add_cog(Giveaway(client))