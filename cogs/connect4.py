import asyncio

import discord
from discord.ext import commands

from game import Connect4Game

class Connect4(commands.Cog):
    CANCEL_GAME_EMOJI = '🚫'
    DIGITS = [str(digit) + '\N{combining enclosing keycap}' for digit in range(1, 8)] + ['🚫']
    VALID_REACTIONS = [CANCEL_GAME_EMOJI] + DIGITS
    GAME_TIMEOUT_THRESHOLD = 60

    def __init__(self, bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
      print("Connect4 cog loaded")

    @commands.command()
    async def c4(self, ctx, *, player2: discord.Member):
      """
      Play connect4 with another player
      """

      if player2.bot:
        await ctx.send("You can't play with a bot!")
        return

      if player2 == ctx.author:
       await ctx.send("You can't play with yourself!")
       return

      player1 = ctx.message.author

      game = Connect4Game(
        player1.display_name,
        player2.display_name
      )

      message = await ctx.send(str(game))

      for digit in self.DIGITS:
        await message.add_reaction(digit)

      def check(reaction, user):
        return (
          user == (player1, player2)[game.whomst_turn()-1]
          and str(reaction) in self.VALID_REACTIONS
          and reaction.message.id == message.id
        )

      while game.whomst_won() == game.NO_WINNER:
        try:
          reaction, user = await self.bot.wait_for(
            'reaction_add',
            check=check,
            timeout=self.GAME_TIMEOUT_THRESHOLD
          )
        except asyncio.TimeoutError:
          game.forfeit()
          break

        await asyncio.sleep(0.2)
        try:
          await message.remove_reaction(reaction, user)
        except discord.errors.Forbidden:
          pass

        if str(reaction) == self.CANCEL_GAME_EMOJI:
          game.forfeit()
          break

        try:
          # convert the reaction to a 0-indexed int and move in that column
          game.move(self.DIGITS.index(str(reaction)))
        except ValueError:
          pass # the column may be full

        await message.edit(content=str(game))

      await self.end_game(game, message)

    @c4.error
    async def c4_error(self,ctx, error):  
      print(error)
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Please mention a player to play with.")
      elif isinstance(error, commands.BadArgument):
          await ctx.send(f"Please make sure to mention/ping a player (ie. {ctx.author.mention}).")

    @classmethod
    async def end_game(cls, game, message):
      await message.edit(content=str(game))
      await cls.clear_reactions(message)

    @staticmethod
    async def clear_reactions(message):
      try:
        await message.clear_reactions()
      except discord.HTTPException:
        pass

def setup(bot):
	bot.add_cog(Connect4(bot))