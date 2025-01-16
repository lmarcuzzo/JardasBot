#FLAGS DEV, MODS, ALL
from discord.ext import commands

async def check_auth(ctx: commands.Context, level: str):        
    try:
        if level == "DEV":
            if (ctx.message.author == 'ruimachado' or 'leomarcuzzo'):
                return True
        elif level == "MODS":
            if (1181373578030104716 in ctx.message.author.roles.id):
                print(ctx.message.author.roles)
                return True
        elif level == "ALL":
            return True
        return False
    except Exception as e:
        await ctx.channel.send(f"Error setting permissions or permission denied: {e}")
        return False
    