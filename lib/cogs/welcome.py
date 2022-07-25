from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command
from random import choice

from ..db import db


class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("welcome")

    @Cog.listener()
    async def on_member_join(self, member):
        db.execute("INSERT INTO exp (UserID) VALUES (?)", member.id)
        await self.bot.get_channel(999416235609555126).send(f"Welcome to **{member.guild.name}** {member.mention}!")

        try:
            await member.send(f"Welcome to **{member.guild.name}**!")
            await member.send(f"{choice(('https://tenor.com/view/the-mandalorian-baby-yoda-the-child-star-wars-cute-gif-16181871', 'https://tenor.com/view/baby-yoda-hi-hello-greet-wave-gif-15912640', 'https://tenor.com/view/the-mandalorian-the-child-baby-yoda-cute-wave-gif-16214706', 'https://tenor.com/view/hello-there-baby-yoda-mandolorian-hello-gif-20136589', 'https://tenor.com/view/baby-yoda-gif-19161736'))}")

        except Forbidden:
            pass

        # make sure these roles are not at the top - above any admin roles or there will be an error
        # await member.add_roles(member.guild.get_role(1000485792264753215), member.guild.get_role(1000477037951193228))

    @Cog.listener()
    async def on_member_remove(self, member):
        db.execute("DELETE FROM exp WHERE UserID = ?", member.id)
        await self.bot.get_channel(999416235609555126).send(f"{member.display_name} has left {member.guild.name}.")


def setup(bot):
    bot.add_cog(Welcome(bot))