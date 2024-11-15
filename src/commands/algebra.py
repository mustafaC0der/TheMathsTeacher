from discord.ext import commands
from sympy import symbols, Eq, solve

class Algebra(commands.Cog):
    """Commands for solving algebraic equations."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="solve")
    async def solve_equation(self, ctx, *, equation: str):
        """Solves a simple algebraic equation with one variable (x)."""
        try:
            x = symbols('x')
            eq = Eq(eval(equation.replace("=", ",")))
            solutions = solve(eq, x)
            await ctx.send(f"📐 Solutions: `{solutions}`")
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

def setup(bot):
    bot.add_cog(Algebra(bot))
