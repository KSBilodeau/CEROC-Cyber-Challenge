import discord
import logging

from discord import app_commands
from discord.ext import commands
from firebase_admin import db
from modals import AddChallengeModal

logger = logging.getLogger("discord.challenge")


class Challenge(commands.Cog):
    group = app_commands.Group(name="challenge", description="Manage active challenges and your submissions.")
    users = db.reference("users")
    challenges: db.Reference = db.reference("challenges")

    @group.command()
    async def search(self, interaction: discord.Interaction, query: str):
        await interaction.response.defer(ephemeral=True)
        embed = discord.Embed(title="Challenge Search", color=0x4e5d94, description=f'Your query was "{query}"!')

        challenge_dict = self.challenges.get()
        if isinstance(challenge_dict, dict):
            for key, value in challenge_dict.items():
                if query.lower() in value["name"].lower() and query.lower() in value["content"].lower():
                    embed.add_field(name=(value["name"] + " [" + key + "]"), value=(value["content"][0:125] + "…"))

        if len(embed.fields) == 0:
            embed.add_field(name="Error", value="No results were found for your query!")

        await interaction.followup.send(embed=embed)

    @group.command()
    async def list(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        embed = discord.Embed(title="Challenge List", color=0x4e5d94)

        challenges_dict = self.challenges.get()
        if isinstance(challenges_dict, dict):
            for key, value in challenges_dict.items():
                embed.add_field(name=(value["name"] + " [" + key + "]"), value=(value["content"][0:125] + "…"))

        if len(embed.fields) == 0:
            embed.description = "No challenges are currently available!"

        await interaction.followup.send(embed=embed)

    @group.command()
    async def submit(self, interaction: discord.Interaction, challenge_id: int, string: str = None,
                     number: int = None, file: discord.Attachment = None):
        await interaction.response.defer(ephemeral=True)
        message = f'Receipt of submission for Challenge #{int(challenge_id)}:\n```'

        if string is not None:
            message += f'Str Flag:\n\t"{string}"\n'

        if number is not None:
            message += f'Num Flag:\n\t{int(number)}\n'

        if file is not None:
            message += "File Flag:\n"
            message += f'\tName: {file.filename}\n'
            message += f'\tSize: {file.size}\n'
            message += f'\tDesc: "{file.description}"\n'

        message += "```"

        await interaction.followup.send(message)

    @group.command()
    async def add(self, interaction: discord.Interaction):
        await interaction.response.send_modal(AddChallengeModal())


async def setup(bot: commands.Bot):
    await bot.add_cog(Challenge())
    logger.info("Extension loaded successfully!")


async def teardown(_: commands.Bot):
    logger.info("Extension unloaded successfully!")
