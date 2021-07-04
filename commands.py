import discord
import serverhandler
from builtins import bot
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self):
        self.bot = bot
        self.server = serverhandler.SCPSL("127.0.0.1", 886, "abc")

    @commands.command(name="playerlist", help="Shows a list of players currently on the server", aliases=['pl'])
    async def playerlist(self, ctx):
        players = self.server.get_player_list()
        if players is not None:
            players = players.split(",")
            del players[-1]
            message = ""
            for x in range(0, len(players), 3):
                message += f"`{players[x]}` - `{players[x + 1]}` - `{players[x + 2]}`\n"
        else:
            message = "No Players Online."
        await ctx.send(embed=discord.Embed(title="Players Online:", description=message))

    @commands.command(name="uptime", help="Shows how long the server has been running (in minutes)")
    async def uptime(self, ctx):
        await ctx.send(embed=discord.Embed(title="Server Uptime:", description=self.server.get_uptime()))

    @commands.has_permissions(administrator=True)
    @commands.command(name="broadcast", help="Broadcasts a message to the server.")
    async def broadcast(self, ctx, *, message):
        broadcast = self.server.broadcast(message)
        await ctx.send(broadcast)

    @commands.has_permissions(administrator=True)
    @commands.command(name="ban", help="Bans a player for a month. (Uses the small number for the ID.)")
    async def ban(self, ctx, *, to_ban):
        to_ban = to_ban.split(" ")
        banned = self.server.ban_player(to_ban)
        await ctx.send(banned)

    @commands.has_permissions(administrator=True)
    @commands.command(name="kick", help="Kick a player. (Uses the small number for the ID.)")
    async def kick(self, ctx, *, to_kick):
        to_kick = to_kick.split(" ")
        kicked = self.server.kick_player(to_kick)
        await ctx.send(kicked)
