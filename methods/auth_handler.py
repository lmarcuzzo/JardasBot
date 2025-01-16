#FLAGS DEV, MODS, ALL
from discord.ext import commands

async def check_auth(ctx: commands.Context, level: str):        
    try:
        if level == "DEV":
            if (ctx.message.author == 'ruimachado' or 'leomarcuzzo'):
                return True
        elif level == "MODS":
            for role in ctx.message.author.roles:
                if(role.id == 1181373578030104716):
                    return True
            return False
        elif level == "ALL":
            return True
        return False
    except Exception as e:
        await ctx.channel.send(f"Error setting permissions or permission denied: {e}")
        return False
    