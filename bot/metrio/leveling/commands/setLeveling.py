import nextcord
from nextcord.ext import commands
from src.dictionaries import level


class SetLeveling(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-discord-set-leveling",
        description="Activate leveling on your Discord",
        force_global=True,
        default_member_permissions=8
    )
    async def set_leveling(
            self,
            ctx: nextcord.Interaction,
            leveling_status: str = nextcord.SlashOption(choices=["True", "False"], required=True),
            leveling_speed: int = nextcord.SlashOption(required=False, default=1)
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :param leveling_status:
        :param leveling_speed:
        :return: None
        ----------
        """

        await level.set_leveling(
            server_id=ctx.guild.id,
            leveling_setting=leveling_status,
            leveling_speed=leveling_speed
        )
        await ctx.send(f"Leveling Status set to: {leveling_status}", ephemeral=True)


def setup(bot):
    bot.add_cog(SetLeveling(bot))
