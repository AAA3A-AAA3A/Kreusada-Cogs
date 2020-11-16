import discord
from validator_collection import validators
from datetime import datetime
from redbot.core import commands, checks, Config, modlog
from .staffembed import Embed

class Staff(commands.Cog):
    """Cog for alerting Staff."""

    def __init__(self):
        self.config = Config.get_conf(
            self, 200730042020, force_registration=True)
        default_guild = {
            "role": None,
            "channel": None
        }
        self.config.register_guild(**default_guild)
        
    @commands.group()
    async def staffset(self, ctx):
        """Staff notifier configuration."""

    @staffset.command()
    @commands.mod()
    async def channel(self, ctx, channel: discord.TextChannel):
        """Sets the channel for staff to receive notifications."""
        await self.config.guild(ctx.guild).set_raw("channel", value=channel.id)
        embed =Embed.create(
            self, ctx, title="Successful <:success:777167188816560168>",
            description=f"{channel.mention} will now receive notifications from users to notify the staff."
        )
        await ctx.send(embed=embed)

    @staffset.command()
    @commands.mod()
    async def role(self, ctx, role: discord.Role):
        """Sets the Staff role."""
        try:
            await self.config.guild(ctx.guild).set_raw("role", value=role.id)
            embed = Embed.create(
                self, ctx, title="Successful <:success:777167188816560168>",
                description=f"{role.mention} will now be considered as the Staff role.",
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            embed = Embed.create(
                self, ctx, title="Oopsies! <:error:777117297273077760>",
                description=f"Something went wrong during the setup process."
            )
            await ctx.send(embed=embed)

    @commands.command()
    #@commands.cooldown(1, 600, commands.BucketType.user)
    async def staff(self, ctx):
        """Notifies the staff."""
        embed = Embed.create(
            self, ctx, title=':alert: The Staff have been notified.',
            description = (
                "Please keep your cool, and if required, try to disperse the situation. "
                "A member of our Staff team will be with you as soon as possible."
                )
        )
        await ctx.send(embed=embed)
        role = ctx.guild.get_role(await self.config.guild(ctx.guild).get_raw("role"))
        chan = await self.config.guild(ctx.guild).get_raw("channel")
        bot = self.bot
        channel = ctx.guild.get_channel(chan) if chan is not None\
            else ctx.channel
        if role is not None:
            embed = Embed.create(
                self, ctx, title=':alert: ALERT!',
                description=f"**{ctx.author.name}** has just called for the staff in {ctx.channel.mention}.\n\n"
            )
            msg = await channel.send(content=role.mention, allowed_mentions=discord.AllowedMentions(roles=True), embed=embed, delete_after=43200)
            await msg.add_reaction("✅")
        reaction, user = await self.bot.wait_for("reaction_add", check = check)
        if reaction == ("✅"):
            await reaction.message.delete
            await channel.send("Yeet")
        else:
            embed = Embed.create(
                self, ctx, title="The Staff team have not completed the command setup. <:error:777117297273077760>",
                description=(
                    "This is a requirement for the staff command to function.\n"
                )
            )
            await ctx.send(embed=embed)
