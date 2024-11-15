from discord.ext import commands
from utils.math_helpers import evaluate_expression

class MathCommands(commands.Cog):
    """Commands for solving math problems."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calc")
    async def calculate(self, ctx, *, expression: str):
        """Evaluates a mathematical expression."""
        try:
            result = evaluate_expression(expression)
            await ctx.send(f"🧮 The result is: `{result}`")
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

def setup(bot):
    bot.add_cog(MathCommands(bot))
