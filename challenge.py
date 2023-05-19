import discord
import logging

from discord import app_commands
from discord.ext import commands
from firebase_admin import db

logger = logging.getLogger("discord.challenge")


class Challenge(commands.Cog):
    # Store a reference to the command group to connect the extension commands all together
    group = app_commands.Group(name="challenge", description="Manage active challenges and your submissions.")

    # Retrieve and store references to the top level database objects
    users: db.Reference = db.reference("users")
    challenges: db.Reference = db.reference("challenges")

    @group.command()
    async def search(self, interaction: discord.Interaction, query: str):
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(f'Your query was "{query}"!')

    @group.command()
    async def list(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(f'There are no available challenges yet!')

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


async def setup(bot: commands.Bot):
    await bot.add_cog(Challenge())
    logger.info("Extension loaded successfully!")


async def teardown(bot: commands.Bot):
    logger.info("Extension unloaded successfully!")
