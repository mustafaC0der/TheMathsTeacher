from discord.ext import commands
from statistics import mean, median

class Statistics(commands.Cog):
    """Commands for basic statistical calculations."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mean")
    async def calculate_mean(self, ctx, *numbers: float):
        """Calculates the mean (average) of a list of numbers."""
        try:
            result = mean(numbers)
            await ctx.send(f"📊 Mean: `{result}`")
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

    @commands.command(name="median")
    async def calculate_median(self, ctx, *numbers: float):
        """Calculates the median of a list of numbers."""
        try:
            result = median(numbers)
            await ctx.send(f"📊 Median: `{result}`")
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

def setup(bot):
    bot.add_cog(Statistics(bot))
