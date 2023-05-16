import discord

from discord import ui
from firebase_admin import db


class AddChallengeModal(ui.Modal, title="Create a Challenge"):
    challenges = db.reference("challenges")

    name = ui.TextInput(label="Name?", style=discord.TextStyle.short, placeholder="Pen Pineapple Apple Pen",
                        required=True)
    desc = ui.TextInput(label="Short Description?", style=discord.TextStyle.short, placeholder="What is the challenge?")
    body = ui.TextInput(label="Challenge Content?", style=discord.TextStyle.paragraph,
                        placeholder="Prompt for the challenge",
                        required=True)
    flag = ui.TextInput(label="Flag?", style=discord.TextStyle.paragraph, placeholder="INSERT_CHALLENGE_FLAG_HERE",
                        required=True)

    async def on_submit(self, interaction: discord.Interaction):
        self.challenges.push({
            'name': self.name.value,
            'content': self.body.value,
            "description": self.desc.value,
            'flag': self.flag.value,
            'active': True
        })

        await interaction.response.send_message("Challenge added!", ephemeral=True)
