#Libraries 
import discord
import asyncio
from discord.ext import commands

#===========================

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print("Moderation cog loaded")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=1):
      if amount < 101:
        if (amount <= 0):
          embedn01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE N01** \nNegative Value\n\nAre you stupid? you cant have negative numbers to clear messages. It should be something like this: ssbc.clear 10 <---- whole number\n\nSometimes I question your intellegence my friend", color=(16737304))
          return await ctx.send(embed=embedn01)
        await ctx.channel.purge(limit=amount +1)
        msg = await ctx.send(f"**{amount}** messages successfully deleted at the speed of sound, if they didn't this means there's an error.")
        await asyncio.sleep(5)
        await msg.delete()
      else:
        await ctx.send("You are exceeding the limit of 100 messages per use")

    @clear.error
    async def clear_error(self,ctx, error):
      if isinstance(error, commands.MissingPermissions):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
      if isinstance(error, commands.BotMissingPermissions):
        embedb01c = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE B01** \nInsufficient Permissions\n\nI do not have permissions to clear messages.\nI need the ``manage messages`` permission.\n\nIf you are still seeing this message, please contact the developer.", color=(16737304))
        await ctx.send(embed=embedb01c)
      else:
        raise error

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member : discord.Member, *, reason=None):
      if member == None or member == ctx.message.author:
        embeds01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE S01**\n\nYou cannot ban yourself stupid", color=(16737304))
        await ctx.channel.send(embed=embeds01)
        return
      if reason == None:
        reason = "No reason specified"
      await member.create_dm()
      embedofbandm = discord.Embed(title=f"{member.name}, You've been banned from: \n`{ctx.guild.name}`", description=f'**Reason:** {reason}', color=(16737304))
      await member.dm_channel.send(embed=embedofbandm)
      await member.ban(reason=reason)
      embedofban = discord.Embed(title="🔨Ban Successful🔨", description=f'**Member Banned:** <@!{member.id}>\n **Reason:** {reason}', color=(16737304))
      await ctx.send(embed=embedofban)

    @ban.error
    async def ban_error(self,ctx, error):
     if isinstance(error, commands.MissingPermissions):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``ban members`` permission\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
     else:
        raise error

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
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

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member : discord.Member, *, reason=None):
      if member == None or member == ctx.message.author:
        embeds01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE S01**\n\nYou cannot kick yourself stupid", color=(16737304))
        await ctx.channel.send(embed=embeds01)
        return
      if reason == None:
          reason = "No reason specified"
          await member.create_dm()
          embedofkickeddm = discord.Embed(title=f"{member.name}, You've been kicked from: \n`{ctx.guild.name}`", description=f'**Reason:** {reason}', color=(16737304))
          await member.dm_channel.send(embed=embedofkickeddm)
          await member.kick(reason=reason)
          embedofkicked = discord.Embed(title="🔧Kick Successful🔧", description=f'**Member Kicked:** <@!{member.id}>\n **Reason:** {reason}', color=(16737304))
          await ctx.send(embed=embedofkicked)

    @kick.error
    async def kick_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command.\nYou need the ``kick members`` permission\n\nAsk a server Admin for help", color=(16737304))
            await ctx.send(embed=embedm01)
        else:
            raise error

    @commands.command()
    async def mute(self,ctx, member : discord.Member, *, reason=None):
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

    @commands.command()
    async def unmute(self,ctx, member : discord.Member, *, reason=None):
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

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def snipe(self,ctx):
      try:
        contents, author, channel_name, time = commands.sniped_messages[ctx.guild.id]
        
      except:
        await ctx.channel.send("Could not find any message to snipe. Please snipe a deleted message next time")
        return

      embed = discord.Embed(description=contents, color=(16737304), timestamp=time)
      embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
      embed.set_footer(text=f"Deleted in : #{channel_name}")

      await ctx.channel.send(embed=embed)

    @snipe.error
    async def snipe_error(self,ctx, error):
     if isinstance(error, commands.MissingPermissions):
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
     else:
        raise error

    @commands.command(pass_test=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def nuke(self,ctx, amount=10**10):
      if not ctx.author.permissions_in(ctx.channel).manage_messages:
        embedm01 = discord.Embed(description="**AN ERROR HAS OCCURRED - ERROR CODE M01** \nMissing Permissions\n\nSorry, you are not allowed to use this command. You need the ``manage messages`` permission\n\nAsk a server Admin for help", color=(16737304))
        await ctx.send(embed=embedm01)
        return
      await ctx.channel.purge(limit=amount)
      await ctx.send('Channel successfully nuked at the speed of sound.\nhttps://imgur.com/LIyGeCR')
      return

    @nuke.error
    async def nuke_error(self,ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
          msg = 'Ayo, calm down! This command has a cooldown, please try again in {:.2f}s'.format(error.retry_after)
          await ctx.send(msg)
      else:
          raise error

def setup(client):
    client.add_cog(moderation(client))