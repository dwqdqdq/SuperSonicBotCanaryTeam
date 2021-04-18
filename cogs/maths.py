import discord 
from discord.ext import commands
import random
import math

@commands.Cog.listener()
async def on_ready(self):
  print("Maths cog loaded")

def add(n: float, n2: float):
  return n + n2

def sub(n: float, n2: float):
  return n - n2

def rando(n: int, n2: int):
  return random.randint(n, n2)

def div(n: float, n2: float):
  return n / n2

def sqrt(n: float):
  return math.sqrt(n)

def mult(n: float, n2: float):
  return n * n2

class Maths(commands.Cog):

  def __init__(self, client):
    self.client = client 

  class Maths(commands.Cog):
    def __init__(self,client):
      self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("Math Cog loaded")
  
  @commands.command()
  async def mathadd(self,ctx,x:int,y:int):
    try:
      result = add(x,y)
      await ctx.send(f"**Number Added:** {result}")
    except:
      pass
  
  @commands.command()
  async def mathsub(self,ctx, x: int, y: int):
    try:
      result = sub(x, y)
      await ctx.send(f"**Number Subtracted:** {result}")

    except:
      pass
    
  @commands.command()
  async def mathrando(self,ctx, x: float, y: float):
    try:
      result = rando(x, y)
      await ctx.send(result)

    except:
      pass
  
  @commands.command()
  async def mathdiv(self,ctx, x: float, y: float):
    try:
      result = div(x, y)
      await ctx.send(f"**Number Divided:** {result}")

    except:
      pass
  
  @commands.command()
  async def mathmult(self,ctx, x: float, y: float):
    try:
      result = mult(x, y)
      await ctx.send(f"**Number Multiplied:** {result}")

    except:
      pass

  @commands.command()
  async def mathsqrt(self,ctx, x: float):
    try:
      result = sqrt(x)
      await ctx.send(result)

    except:
      pass
  
def setup(client):
  client.add_cog(Maths(client))