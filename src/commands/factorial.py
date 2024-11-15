from discord.ext import commands
from math import factorial

class Factorial(commands.Cog):
    """Commands for calculating factorials."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="factorial")
    async def calculate_factorial(self, ctx, number: int):
        """Calculates the factorial of a given number."""
        if number < 0:
            await ctx.send("❌ Error: Factorial is not defined for negative numbers.")
        else:
            result = factorial(number)
            await ctx.send(f"🎲 Factorial of {number} is `{result}`")

def setup(bot):
    bot.add_cog(Factorial(bot))
