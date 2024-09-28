import discord
import logging

from discord import app_commands
from discord.ext import commands

logger = logging.getLogger("discord.challenge")


class Challenge(commands.Cog):
    group = app_commands.Group(name="challenge", description="Manage active challenges and your submissions.")

    @group.command()
    async def search(self, interaction: discord.Interaction, query: str):
        # Necessary for all commands, ensures the message is only available to the user
        await interaction.response.defer(ephemeral=True)
        # Dummy embed created as a starting point and test
        embed = discord.Embed(title="Challenge Search", color=0x4e5d94, description=f'Your query was "{query}"!')
        # Necessary to complete an interaction, as it sends the embed
        await interaction.followup.send(embed=embed)

    @group.command()
    async def list(self, interaction: discord.Interaction):
        # Necessary for all commands, ensures the message is only available to the user
        await interaction.response.defer(ephemeral=True)
        # Dummy embed created as a starting point and test
        embed = discord.Embed(title="Challenge List", color=0x4e5d94)
        # Necessary to complete an interaction, as it sends the embed
        await interaction.followup.send(embed=embed)

    @group.command()
    async def submit(self, interaction: discord.Interaction, challenge_id: int, flag: str):
        # Necessary for all commands, ensures the message is only available to the user
        await interaction.response.defer(ephemeral=True)
        # Not all followups are embeds!  You can also send strings.
        await interaction.followup.send(f'You submitted:\nChallenge ID: {challenge_id}\nChallenge Flag: {flag}')

    @group.command()
    async def add(self, interaction: discord.Interaction):
        # This function should be sending a modal, but for the sake of the skeleton, it'll defer
        await interaction.response.defer(ephemeral=True)
        # Dummy response as this function would normally send a modal
        await interaction.followup.send("THIS IS A TEST")

    @group.command()
    async def end(self, interaction: discord.Interaction, challenge_id: int):
        # Necessary for all commands, ensures the message is only available to the user
        await interaction.response.defer(ephemeral=True)
        # Not all followups are embeds!  You can also send strings.
        await interaction.followup.send(f'You have asked to end Challenge #{challenge_id}')


async def setup(bot: commands.Bot):
    await bot.add_cog(Challenge())
    logger.info("Extension loaded successfully!")


async def teardown(_: commands.Bot):
    logger.info("Extension unloaded successfully!")
