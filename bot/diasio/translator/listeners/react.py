import nextcord
from nextcord.ext import commands
from deep_translator import GoogleTranslator
from src.loader.jsonLoader import Diasio


class TranslatorReact(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        supported_languages = Diasio().get_supported_languages()
        emote = bytes(str(payload.emoji), "utf-8")
        key = str(emote).replace("\\", "")[2:-1]
        user = payload.member

        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        embed_translation = nextcord.Embed(title=self.bot.user.name, description="Fun | Diasio", color=nextcord.Color.dark_gold())

        try:
            language = supported_languages[key]
        except KeyError:
            return

        translator = GoogleTranslator(target=language)
        translation = translator.translate(message.content)

        embed_translation.add_field(name="Translation", value=translation)
        await user.send(embed=embed_translation)


def setup(bot):
    bot.add_cog(TranslatorReact(bot))
