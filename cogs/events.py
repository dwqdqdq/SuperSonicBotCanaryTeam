#Libraries
import discord 
from discord.ext import commands 
import aiofiles
import json

#==========================

class Events(commands.Cog):
    
    commands.sniped_messages = {}
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print("Events cog loaded")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.channel.name + " was invoked incorrectly!")
        print(error)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
      commands.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)



def setup(client):
    client.add_cog(Events(client))